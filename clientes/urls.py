from django.urls import path
from .views import createClient, clientesList, clienteByDocument, deleteClient, updateClient

urlpatterns = [
    path('clientes/', clientesList),
    path('clientes/createCliente/', createClient),  
    path('clientes/<int:document>/', clienteByDocument),  
    path('clientes/deleteClient/<int:document>/', deleteClient),  
    path('clientes/updateClient/<int:document>/', updateClient), 
]
