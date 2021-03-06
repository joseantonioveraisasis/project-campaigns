from datetime import datetime
from gc import get_objects
from genericpath import exists
import pandas as pd
import csv
from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import connection
from django.db.models import Q

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
    DwTemp202206,
    DwProcesosEtl,
    PgStatActivity)
from .forms import CreateForm, UploadFileForm


# Create your views here.

#listar las campañas
class CampaignList(ListView):
    template_name = 'index.html'
    paginate_by = 50
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
    #context_object_name = 'parameters'

    ''' def get_queryset(self):
        context = {'pk':self.kwargs['pk']}
        return context '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
        

    def get_success_url(self, **kwargs):
        return reverse_lazy('campaigns_app:upload', kwargs={'pk': self.kwargs['pk']})
    
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES['file']
        df = pd.read_csv(files,sep=',')
        row_iter = df.iterrows()
        option = request.POST['option']
        objs = []
        lst = list()
        objs2 = []

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
            lst.append(row['cuitcuil'])
            
        to_delete = DwTemp202206.objects.filter(id_campania=pk)
        to_delete.delete()
        DwTemp202206.objects.bulk_create(objs)

        query_clientes = DwClientes.objects.filter(
            cuitcuil__in = lst,
            black_list__id_cliente__isnull=True
        ).values('id_cliente')

        for item in query_clientes:
            _list = DwCampaniaClienteCanal(
                id_campania = pk, 
                id_cliente = item['id_cliente'],
                fecha = datetime.now().strftime("%Y-%m-%d")
            )
            objs2.append(_list)

        DwCampaniaClienteCanal.objects.bulk_create(objs2)
            
        print(f'la consulta: {query_clientes.query}')
        print(f'resultado: {query_clientes}')
        print(f'bulk: {objs2}')


        #k=Enrollment.objects.filter(course__courseid=1).values('id','course__courseid','course__name','enrollid')

        if form.is_valid():
            #print('================valid================')
            return self.form_valid(form)
        else:
            #print('================invalid================')
            return self.form_invalid(form)


class FiltersView(TemplateView):
    template_name = 'filters.html'
    #extra_context = {'page_name': 'home'}

    '''def get_queryset(self):
        context = self.kwargs['pk']
        return context '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class UploadView(TemplateView):
    template_name = 'upload.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class EmptyView(TemplateView):
    template_name = 'empty.html'


class ProcessView(ListView):
    template_name = 'process.html'
    model = DwProcesosEtl
    paginate_by = 20
    ordering = '-fecha_inicio_proceso'
    context_object_name = 'procesos'


class ActivityView(ListView):
    template_name = 'activity.html'
    model = PgStatActivity
    paginate_by = 20
    ordering = '-query_start'
    context_object_name = 'activity'

    def get_queryset(self):
        queryset = PgStatActivity.objects.filter(
            Q(datname = 'biwares') & ~Q(state='idle')
        )
    
        return queryset



