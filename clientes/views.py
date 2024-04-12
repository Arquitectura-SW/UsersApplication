from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from clientes.logic.logic_clientes import getClientes, createCliente, getClienteByDocumento, deleteClienteByDocumento, updateClienteByDocumento, getClienteByDocumentoVal

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
            is_valid, message = validate_client_data(request.data)
            if not is_valid:
                return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
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

def validate_client_data(client_data):
    id_number = client_data.get('document', None)
    birth_date_str = client_data.get('birthdate', None)
    message = ''
    is_valid = True
    
    if id_number:
        client = getClienteByDocumentoVal(id_number)
        if client is not None:
            message += "The client with the provided document number already exists in the system. "
            is_valid = False

    if birth_date_str:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            message += "The client must be of legal age to register in the system. "
            is_valid = False

    if id_number:
        if len(id_number) != 10:
            message += "The document number (cedula) must have 10 digits."
            is_valid = False

    return is_valid, message if message else None