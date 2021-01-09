from datetime import date

class Asset(object):
    pass

    def __init__(self):
        self.id = 0
        self.customerId = 0
        self.title = ''
        self.type = 0
        self.acquisitionDate = date.today()
        self.estimatedValue = 0
        self.payValue = 0
        self.remainingValue = 0

    def map(self, dto):
        self.customerId = dto["customerId"]
        self.title = dto["title"]
        self.type = dto["type"]
        self.acquisitionDate = dto["acquisitionDate"]
        self.estimatedValue = dto["estimatedValue"]
        self.payValue = dto["payValue"]

    def calculate(self):
        self.remainingValue = self.estimatedValue - self.payValue