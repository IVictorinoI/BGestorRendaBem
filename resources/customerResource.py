from flask_restful import Resource
from flask import jsonify, request
from autenticacao import*
from services.customerService import*

class CustomerResouce(Resource):

    def __init__(self):
        pass

    def get(self, cpf=None):
        #AuthToken.autenticar()

        if cpf is None:
            return jsonify(CustomerService().getAll()).json, 200
        else:
            return jsonify(CustomerService().getByCpf(cpf)).json, 200

    def put(self, cpf):
        try:
           #AuthToken.autenticar()
            reg = CustomerService().updateFromPeopleSystem(cpf)
            return jsonify(reg.__dict__).json, 200
        except Exception as e:
            return jsonify({"Message": str(e)}).json, 400

    def delete(self):
        pass

