from django import views
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'campaigns_app'


urlpatterns = [
    path('', views.CampaignList.as_view(), name='index'),
    path('search/', views.CampaignSearch.as_view(), name='search'),
    path('campaign/create/', views.CreateCampaign.as_view(), name='campaign_create'),
    path('load/', views.LoadView.as_view(), name='load'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
