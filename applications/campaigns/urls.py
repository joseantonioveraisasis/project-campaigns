from django import views
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'campaigns_app'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('load/', views.LoadView.as_view(), name='load'),
]
