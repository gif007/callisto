from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('workshop/equipment/', views.equipment, name='equipment'),
    path('store/', views.store, name='store'),
]