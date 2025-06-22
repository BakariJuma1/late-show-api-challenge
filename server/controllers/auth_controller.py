from flask_restful import Resource ,reqparse
from server.models.user import User
from server.app import db
from flask import request

class Register(Resource):
    def post(self):
        # parse incoming requesr data
        data = request.get_json()
        if not data or data.get('username') or not data.get('password'):
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