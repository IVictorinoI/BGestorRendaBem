import requests
import json
from database.customerDb import CustomerDb
from models.customer import Customer
from services.syncronizeCustomerService import SyncronizeCustomerService

class CustomerService(object):
    pass

    def insert(self, dto):
        reg = Customer()
        reg.map(dto)
        return CustomerDb().insert(dto)

    def update(self, id, dto):
        reg = Customer()
        reg.map(dto)
        return CustomerDb().update(id, dto)
    
    def updateFromPeopleSystem(self, cpf):
        dto = SyncronizeCustomerService().getFromPeopleSystem(cpf)

        if(dto == None):
            raise Exception('Nenhum cliente com CPF {0}'.format(cpf))
        
        reg = Customer()
        reg.map(dto)

        self.insertOrUpdateCustomer(cpf, reg)

        return reg

    def insertOrUpdateCustomer(Self, cpf, reg):
        localCustomer = CustomerDb().getByCpf(cpf)

        if(localCustomer == None):
            CustomerDb().insert(reg)
        else:
            CustomerDb().update(localCustomer["id"], reg)

    def getAll(self):
        return CustomerDb().getAll()

    def getByCpf(self, cpf):
        return CustomerDb().getByCpf(cpf)