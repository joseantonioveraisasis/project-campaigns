from datetime import datetime
from genericpath import exists
import pandas as pd
import csv
from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import connection

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.views.generic.edit import FormView

# models
from .models import (
    DwClientes,
    LkClasificacionCampanias, 
    LkClasificacionTracking, 
    DwCampanias, 
    DwCampaniaClienteCanal, 
    DwCampaniaClienteCanalGrupocontrol, 
    DwBlackListGeneral, 
    DwTemp202206)
from .forms import CreateForm, UploadFileForm


# Create your views here.

#listar las campañas
class CampaignList(ListView):
    template_name = 'index.html'
    paginate_by = 15
    ordering = '-fecha_creacion'
    context_object_name = 'camps'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        queryset = DwCampanias.objects_list.list_campaigns(search)
    
        return queryset


#Crear las campañas
class CreateCampaign(CreateView,CreateForm):
    template_name = 'create.html'
    form_class = CreateForm

    def get_success_url(self):
        return reverse_lazy('campaigns_app:load', kwargs={'pk': self.object.pk})

    ''' def form_valid(self, form):
        return super(CreateView, self).form_valid(form) '''


#Editar las campañas
class EditView(UpdateView):
    template_name = 'create.html'
    model = DwCampanias
    form_class = CreateForm

    def get_success_url(self):
        return reverse_lazy('campaigns_app:load', kwargs={'pk': self.object.pk})


#Eliminar las campañas
class DeleteView(DeleteView):
    template_name = 'delete.html'
    model = DwCampanias
    context_object_name = 'camps'
    success_url = reverse_lazy('campaigns_app:index')


class LoadView(FormView):
    form_class = UploadFileForm
    template_name = 'load.html'  # Replace with your template.
    success_url = reverse_lazy('campaigns_app:success')

    ''' def get_queryset(self):
        id = self.kwargs['id']
        return list(id) '''

    

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES['file']
        df = pd.read_csv(files,sep=',')
        row_iter = df.iterrows()
        print(request.POST['inlineRadioOptions'])
        objs = []

        def is_true(llave, dicc):
            if llave in dicc:
                return True

        for i, row in row_iter:

            list_ = DwTemp202206(
                id_campania = pk,
                id_cliente = row['id_cliente'] if is_true('id_cliente',row) else None,
                cuitcuil = row['cuitcuil'] if is_true('cuitcuil',row) else None,
                email = row['email'] if is_true('email',row) else None,
                monto = row['monto'] if is_true('monto',row) else None
            )
            objs.append(list_)
            
        to_delete = DwTemp202206.objects.filter(id_campania=pk)
        to_delete.delete()
        DwTemp202206.objects.bulk_create(objs)

        #k=Enrollment.objects.filter(course__courseid=1).values('id','course__courseid','course__name','enrollid')
        #print(k.query)
        ''' k = DwClientes.objects.filter(
            black_list__id_cliente__isnull=True
        ).values_list('id_cliente')
        print(f'la consulta: {k.query}')
        print(f'resultado: {k}')
 '''
        sql = "select \
                cl.id_cliente,888,'2022-05-19','[mail]' \
                from public.dw_clientes as cl \
                inner join \
                temporal.dw_temp_202206 as t1 on t1.id_cliente = cl.id_cliente \
                left join \
                campanias.dw_black_list_general as bl on bl.id_cliente = cl.id_cliente \
                where \
                bl.id_cliente is null"

        cursor = connection.cursor()
        try:
            cursor.execute(sql)
            row = cursor.fetchall()
            print(row)
        except Exception as e:
            print('############ ERROR #############')
            cursor.close

        if form.is_valid():
            print('================valid================')
            return self.form_valid(form)
        else:
            print('================invalid================')
            return self.form_invalid(form)


class SuccessView(TemplateView):
    template_name = 'success.html'


class EmptyView(TemplateView):
    template_name = 'empty.html'



