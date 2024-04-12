from django.shortcuts import render
from django.contrib import messages
from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse
from clientes.logic.logic_clientes import getClientes, createCliente, getClienteByDocumento, deleteClienteByDocumento, updateClienteByDocumento

@api_view(['GET'])
def clientesList(request):
    if request.method == 'GET':
        clientes = getClientes()
        serializer = ClientSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def clienteByDocument(request, document):
    if request.method == 'GET':
        try:
            client = getClienteByDocumento(document)
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createClient(request):
    if request.method == 'POST':
        try:
            cliente = createCliente(request.data)
            serializer = ClientSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteClient(request, document):
    if request.method == 'DELETE':
        try:
            deleteClienteByDocumento(document)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateClient(request, document):
    if request.method == 'PUT':
        try:
            updateClienteByDocumento(document, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


