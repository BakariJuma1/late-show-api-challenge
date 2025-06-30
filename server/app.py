from flask import Flask
from dotenv import load_dotenv
from server.config import Config
from flask_restful import Api
from server.controllers.auth_controller import Register,Login
from server.controllers.episode_controller import EpisodeList,EpisodeDetail,DeleteEpisode
from server.controllers.guest_controller import GuestList
from server.extension import db,migrate,jwt
from server.controllers.appearance_controller import AppearanceList 

load_dotenv()





def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_prefixed_env()  

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    api = Api(app)

    @app.route('/')
    def home():
        return{"message":"App is running"}
    
    api.add_resource(Register,'/register')
    api.add_resource(Login,'/login')
    api.add_resource(EpisodeList, '/episodes')
    api.add_resource(EpisodeDetail, '/episodes/<int:id>')
    api.add_resource(DeleteEpisode, '/episodes/<int:id>')
    api.add_resource(GuestList, '/guests')
    api.add_resource(AppearanceList, '/appearances')


    return app
