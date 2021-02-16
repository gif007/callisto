from django.urls import path

from . import views

# Web Page Views
urlpatterns = [
    path('', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('workshop/equipment/', views.equipment_all, name='equipment-all'),
    path('workshop/equipment/<str:typ>/<int:pk>', views.equipment, name='equipment'),
    path('workshop/store/', views.store, name='store'),
    path('deploy/', views.deploy, name='deploy'),
]

from . import api

# Deployment API
urlpatterns += [
    path('deploy/get_action/', api.get_action, name='get-action'),
    path('deploy/flee/', api.flee, name='flee'),
    path('deploy/attack/', api.attack, name='attack'),
]


# Equipment API
# urlpatterns += [
#     path('workshop/equipment/<str:typ>/<int:pk>', views.equipment, name='equipment'),
# ]