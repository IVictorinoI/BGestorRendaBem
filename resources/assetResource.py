from flask_restful import Resource
from flask import jsonify, request
from autenticacao import*
from services.assetService import*
import json

class AssetResouce(Resource):

    def __init__(self):
        pass

    def get(self, id=None):
        #AuthToken.autenticar()

        if request.args.get('cpf') is not None:
            return jsonify(json.loads(json.dumps(AssetService().getByCpf(request.args.get('cpf')), indent=2, default=str))).json, 200
        elif id is not None:
            return jsonify(json.loads(json.dumps(AssetService().getById(id), indent=2, default=str))).json, 200
        else:
            return jsonify(json.loads(json.dumps(AssetService().getAll(), indent=2, default=str))).json, 200
        

    def post(self):
        try:
           #AuthToken.autenticar()
            reg = AssetService().insert(request.get_json())
            return jsonify(reg.__dict__).json, 200
        except Exception as e:
            return jsonify({"Message": str(e)}).json, 400

    def put(self, id):
        try:
           #AuthToken.autenticar()
            reg = AssetService().update(id, request.get_json())
            return jsonify(reg.__dict__).json, 200
        except Exception as e:
            return jsonify({"Message": str(e)}).json, 400

    def delete(self):
        pass

