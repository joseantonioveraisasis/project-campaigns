from datetime import datetime
from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
    )
from django.views.generic.edit import FormView

# models
from .models import DwCampanias,LkClasificacionCampanias
from .forms import CreateForm
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        print('+++++++++++++++++++++++++++++++++++++')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('+++++++++++++++++++++++++++++++++++++')
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()
        print('------------------------------------')
    return render(request, 'upload.html', {'form': form})

# Create your views here.

''' class IndexView(TemplateView):
    template_name = 'index.html'


class CreateView(TemplateView):
    template_name = 'create.html' '''

class SuccessView(TemplateView):
    template_name = 'success.html'

class LoadView(FormView):
    template_name = 'load.html'
    form_class = UploadFileForm


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
