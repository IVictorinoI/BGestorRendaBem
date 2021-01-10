from database.assetDb import AssetDb
from models.asset import Asset

class AssetService(object):
    pass

    def insert(self, dto):
        reg = Asset()
        reg.map(dto)
        reg.calculate()
        return AssetDb().insert(reg)

    def update(self, id, dto):
        reg = Asset()
        reg.map(dto)
        reg.calculate()
        return AssetDb().update(id, reg)

    def getAll(self):
        return AssetDb().getAll()
        
    def getByCpf(self, cpf):
        return AssetDb().getByCpf(cpf)

    def getById(self, id):
        return AssetDb().getById(id)