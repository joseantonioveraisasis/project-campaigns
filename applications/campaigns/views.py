from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CreateView(TemplateView):
    template_name = 'create.html'

class LoadView(TemplateView):
    template_name = 'load.html'
