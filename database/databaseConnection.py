import psycopg2



class DatabaseConnection(object):
    pass

    def get(self):
        con = psycopg2.connect(
            host='localhost', 
            database='bgestorrendabem', 
            user='TestUser', 
            password='masterkey'
        )
        return con