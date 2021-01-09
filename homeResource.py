from flask_restful import Resource

class HomeResource(Resource):

    def __init__(self):
        pass

    def get(self):        
        return "Rodando API"

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

