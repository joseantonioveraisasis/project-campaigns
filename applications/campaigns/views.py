from datetime import datetime
import pandas as pd
import csv
from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import FileFieldForm

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
    )
from django.views.generic.edit import FormView

# models
from .models import DwCampanias,LkClasificacionCampanias
from .forms import CreateForm


# Create your views here.

''' class IndexView(TemplateView):
    template_name = 'index.html'


class CreateView(TemplateView):
    template_name = 'create.html' '''

class SuccessView(TemplateView):
    template_name = 'success.html'

class LoadView(FormView):
    form_class = FileFieldForm
    template_name = 'load.html'  # Replace with your template.
    success_url = reverse_lazy('campaigns_app:success')
    

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES['file_field']
        df=pd.read_csv(files,sep=',')
        row_iter = df.iterrows()
        

        for index, row in row_iter:
            print(row[0])

        if form.is_valid():
            return self.form_valid(form)
        else:
            print('================else================')
            return self.form_invalid(form)


#Custom
class CampaignList(ListView):
    template_name = 'index.html'
    paginate_by = 10
    ordering = '-fecha_creacion'
    context_object_name = 'camps'

    def get_queryset(self):
    
        return DwCampanias.objects_create.list_campaigns()
        

class CampaignSearch(ListView):
    template_name = 'index.html'
    paginate_by = 10
    ordering = '-fecha_creacion'
    context_object_name = 'camps'

    def get_queryset(self):
        query = self.request.GET.get('q','')

        return DwCampanias.objects_search.search_campaigns(query)


class CreateCampaign(CreateView,CreateForm):
    template_name = 'create.html'
    model = DwCampanias
    
    form_class = CreateForm
    success_url = reverse_lazy('campaigns_app:load')

    def get_queryset(self):

        return DwCampanias.objects_create.list_campaigns()

    def form_valid(self, form):
        return super(CreateView, self).form_valid(form)
