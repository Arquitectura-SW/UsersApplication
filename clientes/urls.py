from django.urls import path
from .views import createClienteR, clientesList, clienteByDocument, deleteClient, updateClient

urlpatterns = [
    path('clientes/', clientesList),
    path('clientes/createCliente/', createClienteR),  
    path('clientes/<int:document>/', clienteByDocument),  
    path('clientes/delete/<int:document>/', deleteClient),  
    path('clientes/updateClient/<int:document>/', updateClient), 
]
