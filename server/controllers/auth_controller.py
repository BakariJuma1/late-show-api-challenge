from flask_restful import Resource ,reqparse
from server.models.user import User
from server.extension import db
from flask import request
from flask_jwt_extended import create_access_token
from datetime import datetime,timedelta

class Register(Resource):
    def post(self):
        
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return {"Error":"Username and password are required"},400
        
        # extract values from data dict and store in this variables
        username = data['username']
        password = data['password']

        # check if user exists
        if User.query.filter_by(username=username).first():
            return {"Error":"User already exists"},409
        
        user = User(username=username)
        # calling the set passwd fn in models
        user.set_password(password)

        # save to db
        db.session.add(user)
        db.session.commit()

        return {"message":"User created succesfully "},201

class Login(Resource):
    def post(self):

        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return {"Error":"Username and password are required"}
        
        username= data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            token = create_access_token(
                identity=user.id,
                expires_delta=timedelta(hours=1)
            )
            return {"access_token":token},200
        
        return {"error":"Invalid credentials"}
