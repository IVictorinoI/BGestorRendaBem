import psycopg2

from database.databaseConnection import DatabaseConnection

class AssetDb(object):
    pass

    def insert(self, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'INSERT INTO public."Assets"("CustomerId", "Title", "Type", "AcquisitionDate", "EstimatedValue", "PayValue", "RemainingValue") VALUES({0}, \'{1}\', {2}, \'{3}\', {4}, {5}, {6}) RETURNING "Id"'
        
        sql = command.format(reg.customerId, reg.title, reg.type, reg.acquisitionDate, reg.estimatedValue, reg.payValue, reg.remainingValue)
        print(sql)
        cur.execute(sql)

        reg.id = cur.fetchone()[0]

        con.commit()

        con.close()
        return reg

    def update(self, id, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'UPDATE public."Assets" SET "CustomerId"={0}, "Title"=\'{1}\', "Type"={2}, "AcquisitionDate"=\'{3}\', "EstimatedValue"={4}, "PayValue"={5}, "RemainingValue"={6} WHERE "Id"={7}'
        sql = command.format(reg.customerId, reg.title, reg.type, reg.acquisitionDate, reg.estimatedValue, reg.payValue, reg.remainingValue, id)
        print(sql)
        cur.execute(sql)

        reg.id = id

        con.commit()

        con.close()
        return reg

    def getAll(self):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "CustomerId", "Title", "Type", "AcquisitionDate", "EstimatedValue", "PayValue", "RemainingValue", "Status" from "Assets"')
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results

    def getById(self, id):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "CustomerId", "Title", "Type", "AcquisitionDate", "EstimatedValue", "PayValue", "RemainingValue", "Status" from "Assets" where "Id" = {0}'.format(id))
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results

    def getByCpf(self, cpf):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "CustomerId", "Title", "Type", "AcquisitionDate", "EstimatedValue", "PayValue", "RemainingValue", "Status" from "Assets" where exists(select 1 from "Customer" c where c."Id" = "Assets"."CustomerId" and c."Cpf"=\'{0}\')'.format(cpf))
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results        

    def mapToDto(self, data):
        columns = ("id", "customerId", "title", "type", "acquisitionDate", "estimatedValue", "payValue", "remainingValue", "status")

        results = []
        for row in data:
            results.append(dict(zip(columns, row)))

        return results