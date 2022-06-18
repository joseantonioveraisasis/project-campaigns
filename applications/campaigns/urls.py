from django import views
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'campaigns_app'


urlpatterns = [
    path('', views.CampaignList.as_view(), name='index'),
    path('campaign/search/', views.CampaignList.as_view(), name='search'),
    path('campaign/create/', views.CreateCampaign.as_view(), name='campaign_create'),
    path('campaign/load/<pk>/', views.LoadView.as_view(), name='load'),
    path('campaign/success/', views.SuccessView.as_view(), name='success'),
    path('campaign/empty/<pk>/', views.EmptyView.as_view(), name='empty'),
    path('campaign/edit/<pk>/', views.EditView.as_view(), name='edit'),
    path('campaign/delete/<pk>/', views.DeleteView.as_view(), name='delete'),
]
