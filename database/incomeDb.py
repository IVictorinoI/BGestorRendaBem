import psycopg2

from database.databaseConnection import DatabaseConnection

class IncomeDb(object):
    pass

    def insert(self, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'INSERT INTO public."Income" ("CustomerId", "Fixed", "Value") VALUES({0}, {1}, {2})  RETURNING "Id"'
        sql = command.format(reg.customerId, reg.fixed, reg.value)
        print(sql)
        cur.execute(sql)

        reg.id = cur.fetchone()[0]

        con.commit()

        con.close()
        return reg

    def update(self, id, reg):
        con = DatabaseConnection().get()
        cur = con.cursor()

        command = 'UPDATE public."Income" SET "CustomerId"={0}, "Fixed"={1}, "Value"={2} WHERE "Id"={3}'
        sql = command.format(reg.customerId, reg.fixed, reg.value, id)
        print(sql)
        cur.execute(sql)

        reg.id = id

        con.commit()

        con.close()
        return reg

    def getAll(self):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "CustomerId", "Fixed", "Value" from "Income"')
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results

    def getById(self, id):
        con = DatabaseConnection().get()
        cur = con.cursor()

        cur.execute('select "Id", "CustomerId", "Fixed", "Value" from "Income" where "Id" = {0}'.format(id))
        recset = cur.fetchall()

        results = self.mapToDto(recset)

        con.close()

        return results        

    def mapToDto(self, data):
        columns = ("id", "customerId", "fixed", "value")

        results = []
        for row in data:
            results.append(dict(zip(columns, row)))

        return results        