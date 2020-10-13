# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:58:29 2020

@author: Pnk
"""

from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes
from database.db import initialize_db
from flask_jwt_extended import JWTManager
from resources.errors import errors
from flask_mail import Mail

app = Flask(__name__)
api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

app.config['JWT_SECRET_KEY'] = 'kjsadifh81793rh1u35183fioasfuk32413fdsfsaxcvvb'

app.config['MONGODB_SETTINGS'] = {
     'host': 'mongodb://localhost/cArtificial'
}

jwt = JWTManager(app)
mail = Mail(app)

initialize_db(app)
initialize_routes(api)

app.run()


 
# cars = [
#         {
#             "name": "Audi",
#             "model": "A4",
#             "year_made": "2004"
#         },
#         {
#             "name": "BMW",
#             "model": "x3",
#             "year_made": "2009"
#         },
#         {
#             "name": "Mercedes-Benz",
#             "model": "B-class",
#             "year_made": "2018"
#         }
# ]

# @app.route('/cars')
# def get_cars():
#     cars = Car.objects().to_json()
#     return Response(cars,mimetype="application/json", status=200)

# @app.route('/cars', methods=['POST'])
# def add_car():
#      body = request.get_json()
#      car = Car(**body).save()
#      id = car.id
#      return {'id': str(id)}, 200

# @app.route('/cars/<id>', methods=['PUT'])
# def update_car(id):
#     body = request.get_json()
#     Car.objects.get(id=id).update(**body)
#     return '', 200

# @app.route('/cars/<id>', methods=['DELETE'])
# def delete_movie(id):
#     Car.objects.get(id=id).delete()
#     return '', 200

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://localhost/cArtificial'
# }
