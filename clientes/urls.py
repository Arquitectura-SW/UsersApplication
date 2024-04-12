from django.urls import path
from .views import postCliente, clientesList

urlpatterns = [
    path('clientes/', clientesList),
    path('clientes/createCliente', postCliente, name = 'createCliente' )
]