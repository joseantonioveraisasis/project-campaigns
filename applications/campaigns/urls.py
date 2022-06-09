from django import views
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'campaigns_app'


urlpatterns = [
    path('', views.CampaignList.as_view(), name='index'),
    path('search/', views.CampaignSearch.as_view(), name='search'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('load/', views.LoadView.as_view(), name='load'),
]
