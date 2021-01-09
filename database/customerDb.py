import psycopg2

from database.databaseConnection import DatabaseConnection

class CustomerDb(object):
    pass

    def insert(self, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'INSERT INTO public."Customer"("Name", "Cpf", "BirthDate", "Address", "Active") VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', {4}) RETURNING "Id"'
        sql = command.format(reg.name, reg.cpf, reg.birthDate, reg.address, reg.active)
        print(sql)
        cur.execute(sql)

        reg.id = cur.fetchone()[0]

        con.commit()

        con.close()
        return reg

    def update(self, id, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'UPDATE public."Customer" SET "Name"=\'{0}\', "Cpf"=\'{1}\', "BirthDate"=\'{2}\', "Address"=\'{3}\', "Active"={4} WHERE "Id"={5}'
        sql = command.format(reg.name, reg.cpf, reg.birthDate, reg.address, reg.active, id)
        print(sql)
        cur.execute(sql)

        reg.id = id

        con.commit()

        con.close()
        return reg

    def getByCpf(self, cpf):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "Name", "Cpf", "BirthDate", "Address", "Active" from "Customer" where "Cpf"=\'{0}\''.format(cpf))
        recset = cur.fetchall()

        con.close()

        if(len(recset)>0):
            results = self.mapToDto(recset)
            return results[0]

        return None

    def getAll(self):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "Name", "Cpf", "BirthDate", "Address", "Active" from "Customer"')
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results

    def mapToDto(self, data):
        columns = ("id", "name", "cpf", "birthDate", "address", "active")

        results = []
        for row in data:
            results.append(dict(zip(columns, row)))

        return results                