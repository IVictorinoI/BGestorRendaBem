from flask_restful import Resource
from flask import jsonify, request
import json
from autenticacao import*
from services.incomeService import*

class IncomeResouce(Resource):

    def __init__(self):
        pass

    def get(self, id=None):
        #AuthToken.autenticar()

        if id is None:
            return jsonify(json.loads(json.dumps(IncomeService().getAll(), indent=2, default=str))).json, 200
        else:
            return jsonify(json.loads(json.dumps(IncomeService().getById(id), indent=2, default=str))).json, 200


    def post(self):
        try:
           #AuthToken.autenticar()
            reg = IncomeService().insert(request.get_json())
            return jsonify(reg.__dict__).json, 200
        except Exception as e:
            return jsonify({"Message": str(e)}).json, 400

    def put(self, id):
        try:
           #AuthToken.autenticar()
            reg = IncomeService().update(id, request.get_json())
            return jsonify(reg.__dict__).json, 200
        except Exception as e:
            return jsonify({"Message": str(e)}).json, 400

    def delete(self):
        pass

