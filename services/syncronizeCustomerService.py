import requests
import json
from database.customerDb import CustomerDb
from models.customer import Customer

class SyncronizeCustomerService(object):
    pass
    
    def getFromPeopleSystem(self, cpf):
        token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlZpY3RvciIsInJvbGUiOiJEZWZhdWx0Um9sZSIsIklkIjoiNCIsIm5iZiI6MTYxMDIxMzA3MywiZXhwIjoxNjEwMzg1ODczLCJpYXQiOjE2MTAyMTMwNzN9.61BFRLwk5aE2E5-rU1GG9eow4S-sYzSJzWacE0iyRiI'
        apiUrl = 'https://localhost:44373/api/'
        
        response = requests.get('{0}v1/customers/byCpf/{1}'.format(apiUrl, cpf),
                        headers={"content-Type":"application/json", "authorization": token}, verify=False)

        lista = json.loads(response.content)

        if(len(lista) == 0):
            return None

        return lista[0]
