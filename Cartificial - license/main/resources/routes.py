# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:07:56 2020

@author: Pnk
"""

from .cars import CarApi, CarsApi
from .auth import SignupApi,LoginApi
from .pass_reset import ForgotPassword,ResetPassword
    
def initialize_routes(api):
    api.add_resource(CarsApi, '/api/cars')
    api.add_resource(CarApi, '/api/cars/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')