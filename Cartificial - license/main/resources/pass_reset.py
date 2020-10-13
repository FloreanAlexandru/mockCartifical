# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:16:12 2020

@author: Pnk
"""

from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from database.cars_models import User
from flask_restful import Resource
import datetime
from resources.errors import SchemaValidationError, InternalServerError,EmailDoesNotCorrespond, BadTokenError
from jwt.exceptions import ExpiredSignatureError, DecodeError,InvalidTokenError
from services.service_mail import send_email

class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            email = body.get('email')
            if not email:
                raise SchemaValidationError

            user = User.objects.get(email=email)
            if not user:
                raise EmailDoesNotCorrespond

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(str(user.id), expires_delta=expires)

            return send_email('Reset Your Password',
                              sender='support@cArtificial.com',
                              recipients=[user.email],
                              text_body=render_template('email/pass_reset.txt',
                                                        url=url + reset_token),
                              html_body=render_template('email/pass_reset.html',
                                                        url=url + reset_token))
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesNotCorrespond:
            raise EmailDoesNotCorrespond
        except Exception as e:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')

            if not reset_token or not password:
                raise SchemaValidationError

            user_id = decode_token(reset_token)['identity']

            user = User.objects.get(id=user_id)

            user.modify(password=password)
            user.hash_password()
            user.save()

            return send_email('Password reset successful',
                              sender='support@cArtifical.com',
                              recipients=[user.email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except SchemaValidationError:
            raise SchemaValidationError
       # except ExpiredSignatureError:
        #    raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError