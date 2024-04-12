from clientes.models import Cliente

def getClientes():
    return Cliente.objects.all().order_by('document')

def createCliente(formCliente):
    user = formCliente.save()
    user.save()

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
        raise Exception({"error": "Client not saved"}, 404)
    
    
    
