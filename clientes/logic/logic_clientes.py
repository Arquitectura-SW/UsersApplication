from clientes.models import Cliente
from datetime import datetime

def getClientes():
    return Cliente.objects.all().order_by('document')

def createCliente(formCliente):
    try: 
        #is_valid, message = validate_client_data(formCliente)
        #if is_valid:
            user = formCliente.save()
            user.save()
    except: 
        #is_valid, message = validate_client_data(formCliente)
        #if not is_valid:
            raise Exception({'detail': 'No created'}, 400)

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
            user = formCliente.save()
            user.save()
            return Cliente.objects.get(document=document)
    except:
            raise Exception({'detail': message}, 400)
    
    
    
    
    
