from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('workshop/equipment/', views.equipment_all, name='equipment-all'),
    path('workshop/equipment/<str:typ>/<int:pk>', views.equipment, name='equipment'),
    path('workshop/store/', views.store, name='store'),
    path('deploy/', views.deploy, name='deploy'),
    path('deploy/get_action/', views.get_action, name='get-action'),
    path('deploy/flee/', views.flee, name='flee'),
    path('deploy/attack/', views.attack, name='attack'),
]