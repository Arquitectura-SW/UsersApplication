from clientes.models import Cliente
from datetime import datetime

def getClientes():
    return Cliente.objects.all().order_by('document')

def createCliente(formCliente):
    try: 
        is_valid, message = validate_client_data(formCliente)
        if is_valid:
            user = formCliente.save()
            user.save()
    except: 
        if not is_valid:
            raise Exception({'detail': message}, 400)

def createClienteObject(name, lastName, document, birthdate, email, country, city, income, debt, economicActivity, company, profession):
    user = Cliente()
    user.name = name
    user.lastName = lastName
    user.document = document
    user.birthdate = birthdate
    user.email = email
    user.country = country
    user.city = city
    user.income = income
    user.debt = debt
    user.economicActivity = economicActivity
    user.company = company
    user.profession = profession
    user.save()
    
def getClienteByDocumento(document):
    try:
        return Cliente.objects.get(document=document)
    except:
        raise Exception({"error": "Client not found"}, 404)
    
def deleteClienteByDocumento(document):
    try:
        Cliente.objects.delete(document=document)
    except:
        raise Exception({"error": "Client not deleted"}, 404)
    
    
def updateClienteByDocumento(document, formCliente):
    try:
        is_valid, message = validate_client_data(formCliente)
        if is_valid:
            user = formCliente.save()
            user.save()
            return Cliente.objects.get(document=document)
    except:
        if not is_valid:
            raise Exception({'detail': message}, 400)
    
    
# Auxiliary function 
def validate_client_data(client_data):
    id_number = client_data.get('document')
    birth_date_str = client_data.get('birthdate')
    message = ''
    is_valid = True
    
    if id_number:
        client = getClienteByDocumento(id_number)
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

    
    
    
