from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

load_dotenv()
db =SQLAlchemy()
migrate =Migrate()

jwt =JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_prefixed_env()  

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    @app.route('/')
    def home():
        return{"message":"App is running"}

    return app
