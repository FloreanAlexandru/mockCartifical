# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:59:35 2020

@author: Pnk
"""

from flask import Response, request
from database.cars_models import Car, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist,NotUniqueError,DoesNotExist,ValidationError,InvalidQueryError
from resources.errors import InternalServerError,SchemaValidationError,CarAlreadyExistsError,UpdatingCarError,DeletingCarError,CarNotExistsError,UnauthorizedError

class CarsApi(Resource):
    @jwt_required
    def get(self):
        cars = Car.objects().to_json()
        return Response(cars,mimetype="application/json",status=200)
    
    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            car = Car(**body, added_by=user)
            car.save()
            user.update(push__cars=car)
            user.save()
            id = car.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise CarAlreadyExistsError
        except Exception as e:
            raise InternalServerError
            
class CarApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            car = Car.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Car.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingCarError
        except Exception:
            raise InternalServerError  
 
    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            car = Car.objects.get(id=id, added_by=user_id)
            car.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingCarError
        except Exception:
            raise InternalServerError

    @jwt_required
    def get(self, id):
        try:
            cars = Car.objects.get(id=id).to_json()
            return Response(cars, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CarNotExistsError
        except Exception:
            raise InternalServerError