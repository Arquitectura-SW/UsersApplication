from django.urls import path
from .views import createCliente, clientesList, clienteByDocument, deleteClient, updateClient

urlpatterns = [
    path('clientes/', clientesList),
    path('clientes/createCliente', createCliente),
    path('clientes/int<document>', clienteByDocument),
    path('clientes/delete/int<document>', deleteClient),
    path('clientes/updateClient/int<document>', updateClient),
    
]