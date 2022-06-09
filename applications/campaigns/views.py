from re import L
from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView
    )

# models
from .models import DwCampanias,LkClasificacionCampanias

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CreateView(TemplateView):
    template_name = 'create.html'

class LoadView(TemplateView):
    template_name = 'load.html'

#Custom
class CampaignList(ListView):
    template_name = 'index.html'

    def get_queryset(self):
    
        return DwCampanias.objects.list_campaigns()

class CampaignSearch(ListView):
    context_object_name = 'nombre_campania'
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('q','')

        return DwCampanias.objects_search.search_campaigns(query)
