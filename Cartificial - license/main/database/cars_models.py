# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:02:23 2020

@author: Pnk
"""

from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Car(db.Document):
    name = db.StringField(required=True, unique = False)
    model = db.StringField(required=True, unique = False)
    year_made =db.StringField(required=True, unique = False)
    added_by = db.ReferenceField('User')

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    email = db.StringField(required=True, unique=True)
    cars = db.ListField(db.ReferenceField('Car', reverse_delete_rule=db.PULL))
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
     
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
User.register_delete_rule(Car, 'added_by', db.CASCADE)