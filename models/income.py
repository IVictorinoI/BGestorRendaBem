
class Income(object):
    pass

    def __init__(self):
        self.id = 0
        self.customerId = 0
        self.fixed = False
        self.value = 0

    def map(self, dto):
        self.customerId = dto["customerId"]
        self.fixed = dto["fixed"]
        self.value = dto["value"]
