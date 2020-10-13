# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:55:04 2020

@author: Pnk
"""

from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    
    