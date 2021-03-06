# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:54:30 2020

@author: Pnk
"""

from flask import request, Response
from database.cars_models import User
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, UnauthorizedError,InternalServerError,EmailDoesNotCorrespond

class SignupApi(Resource):
 def post(self):
     try:
         body = request.get_json()
         user = User(**body)
         user.hash_password()
         user.save()
         id = user.id
         return {'id': str(id)}, 200
     except FieldDoesNotExist:
            raise SchemaValidationError
     except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
 def post(self):
     try:
       body = request.get_json()
       user = User.objects.get(username=body.get('username'))
       authorized = user.check_password(body.get('password'))
       if not authorized:
         return {'error': 'Email or password invalid'}, 401
     
       expires = datetime.timedelta(days=7)
       access_token = create_access_token(identity=str(user.id), expires_delta=expires)
       return {'token': access_token}, 200
   
     except (UnauthorizedError, DoesNotExist):
        raise UnauthorizedError
     except Exception as e:
        raise InternalServerError