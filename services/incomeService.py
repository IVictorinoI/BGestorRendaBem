from database.incomeDb import IncomeDb
from models.income import Income

class IncomeService(object):
    pass

    def insert(self, dto):
        reg = Income()
        reg.map(dto)
        return IncomeDb().insert(reg)

    def update(self, id, dto):
        reg = Income()
        reg.map(dto)
        return IncomeDb().update(id, reg)

    def getAll(self):
        return IncomeDb().getAll()

    def getById(self, id):
        return IncomeDb().getById(id)        