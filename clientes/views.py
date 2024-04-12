from django.shortcuts import render
from django.contrib import messages
from .forms import clienteForm
from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse
from clientes.logic.logic_clientes import getClientes, createCliente, getClienteByDocumento, deleteClienteByDocumento, updateClienteByDocumento

api_view(['GET'])
def clientesList(request):
    if request.method == 'GET':
        try:
            clientes = getClientes()
            serializer = ClientSerializer(clientes, many= True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
api_view(['GET'])
def clienteByDocument(request, document):
    if request.method == 'GET':
        try:
            client = getClienteByDocumento(document)
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def postCliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            createCliente(form)
            messages.add_message(request, messages.SUCCESS, 'Cliente created successful')
            return HttpResponseRedirect(reverse('createCliente'))
        else:
            print(form.errors)
    else:
        form = clienteForm()

    context = {
        'form': form,
    }

    return render(request, 'clientes/createClientes.html', context)



