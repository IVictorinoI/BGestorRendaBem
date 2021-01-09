from datetime import date

class Customer(object):
    pass

    def __init__(self):
        self.name = ''
        self.cpf = ''
        self.birthDate = date.today()
        self.address = ''
        self.active = True

    def map(self, dto):
        self.name = dto["name"]
        self.cpf = dto["cpf"]
        self.birthDate = dto["birthDate"]
        self.address = dto["address"]
