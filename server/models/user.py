from config import db
from sqlalchemy_serializer import SerializerMixin



class User(db.Model,SerializerMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True)
    