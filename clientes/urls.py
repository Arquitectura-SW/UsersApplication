from django.urls import path
from .views import postCliente, clientesList, clienteByDocument

urlpatterns = [
    path('clientes/', clientesList),
    path('clientes/createCliente', postCliente),
    path('clientes/int<document>', clienteByDocument)
]