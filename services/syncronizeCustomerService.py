import requests
import json
from database.customerDb import CustomerDb
from models.customer import Customer

class SyncronizeCustomerService(object):
    pass
    
    def getFromPeopleSystem(self, cpf):
        token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6InN0cmluZyIsInJvbGUiOiJEZWZhdWx0Um9sZSIsIklkIjoiMSIsIm5iZiI6MTYxMDMwNjU5MiwiZXhwIjoxNjEyODk4NTkyLCJpYXQiOjE2MTAzMDY1OTJ9.UzZjg4e924sYkVBdouc7NSsBUscbXIoPIidTY5m2uN8'
        apiUrl = 'https://localhost:44373/api/'
        
        response = requests.get('{0}v1/customers/byCpf/{1}'.format(apiUrl, cpf),
                        headers={"content-Type":"application/json", "authorization": token}, verify=False)

        lista = json.loads(response.content)

        if(len(lista) == 0):
            return None

        return lista[0]
