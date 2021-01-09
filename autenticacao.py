import jwt
import os
import datetime
from flask import request, abort
from functools import wraps


SECRET_KEY = os.getenv('SECRET_KEY', 'tokentokentoken')

class AuthToken(object):

    def gerarToken(self, value):
        try:
            dto = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
                'iat': datetime.datetime.utcnow(),
                'sub': value
            }        
            return jwt.encode(dto, SECRET_KEY, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def autenticar():                
        assert 'authorization' in request.headers, "Acesso não autorizado"
        try:            
            token = request.headers.get("authorization")
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            return payload['sub']
        except jwt.ExpiredSignatureError as e:
            raise Exception('Login expirado, por favor logue de novo.')
        except jwt.InvalidTokenError:
            raise Exception('Token inválido, por favor logue de novo.')