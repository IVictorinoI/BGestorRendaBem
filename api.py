from flask import Flask, request
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

from homeResource import*
from resources.customerResource import*
from resources.assetResource import*
from resources.incomeResource import*

app = Flask(__name__)
api = Api(app)


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


api.add_resource(HomeResource, '/')
api.add_resource(CustomerResouce, '/customer', '/customer/<cpf>')
api.add_resource(AssetResouce, '/asset', '/asset/<id>')
api.add_resource(IncomeResouce, '/income', '/income/<id>')

if __name__ == '__main__':
    app.run()
