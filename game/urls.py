from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('workshop/equipment/', views.equipment, name='equipment'),
    path('workshop/store/', views.store, name='store'),
    path('deploy/', views.deploy, name='deploy'),
    path('get_action/', views.get_action, name='get-action'),
    path('deploy/flee/', views.flee, name='flee'),
]