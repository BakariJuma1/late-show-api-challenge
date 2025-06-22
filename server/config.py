import os
class Config:
    FLASK_SQLALCHEMY_DATABASE_URI="postgresql://lateshow:1234@localhost:5432/lateshowdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret"