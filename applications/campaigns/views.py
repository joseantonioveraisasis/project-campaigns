from datetime import datetime
import pandas as pd
import csv
from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.views.generic.edit import FormView

# models
from .models import DwCampanias, DwTemp202206,LkClasificacionCampanias
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
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES['file']
        df=pd.read_csv(files,sep=',')
        row_iter = df.iterrows()
        id_campania = '1897'
        objs = [

            DwTemp202206(

                id_campania = '1897',
                cuitcuil = row['cuitcuil'],
                monto = row['monto']


                )

            for index, row in row_iter

        ]
        objects_to_delete = DwTemp202206.objects.filter(id_campania=id_campania)
        objects_to_delete.delete()
        DwTemp202206.objects.bulk_create(objs)
        print('############final#################')


        if form.is_valid():
            return self.form_valid(form)
        else:
            print('================else================')
            return self.form_invalid(form)



        

class CampaignSearch(ListView):
    template_name = 'index.html'
    paginate_by = 10
    ordering = '-fecha_creacion'
    context_object_name = 'camps'

    def get_queryset(self):
        query = self.request.GET.get('q','')

        return DwCampanias.objects_search.search_campaigns(query)


class SuccessView(TemplateView):
    template_name = 'success.html'


class EmptyView(TemplateView):
    template_name = 'empty.html'



