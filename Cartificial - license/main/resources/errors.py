# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:36:32 2020

@author: Pnk
"""

class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class CarAlreadyExistsError(Exception):
    pass

class UpdatingCarError(Exception):
    pass

class DeletingCarError(Exception):
    pass

class CarNotExistsError(Exception):
    pass

class EmailDoesNotCorrespond(Exception):
    pass

class BadTokenError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "CarAlreadyExistsError": {
         "message": "Car with given name already exists",
         "status": 400
     },
     "UpdatingCarError": {
         "message": "Updating car added by other is forbidden",
         "status": 403
     },
     "DeletingCarError": {
         "message": "Deleting car added by other is forbidden",
         "status": 403
     },
     "CarNotExistsError": {
         "message": "Car with given id doesn't exists",
         "status": 400
     },
     "EmailDoesNotCorrespond": {
         "message": " E-mail doesn't correspond to this username",
         "status": 401
     },
     "BadTokenError": {
         "message": " Token is not valid",
         "status": 403
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}