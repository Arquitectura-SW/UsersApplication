from django.shortcuts import render
from django.contrib import messages
from .forms import ClienteForm
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


api_view(['POST'])
def createClient(request, formCliente):
    if request.method == 'POST':
        try:
            createCliente(formCliente)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

api_view(['DELETE'])
def deleteClient(request, document):
    if request.method == 'DELETE':
        try:
            deleteClienteByDocumento(document)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
api_view(['PUT'])
def updateClient(request, document, formCliente):
    if request.method == 'PUT':
        try:
            updateClienteByDocumento(document, formCliente)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    



