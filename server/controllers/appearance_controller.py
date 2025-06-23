from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from server.extension import db
from models import Appearance,Guest,Episode

class AppearanceList(Resource):
    @jwt_required() 
    def post(self):
        data =request.get_json()

        if not data or not all(k in data for k in ('rating', 'guest_id', 'episode_id')):
            return {"error": "rating, guest_id, and episode_id are required"}, 400
        
        rating= data['rating']
        guest_id = data['guest_id']
        episode_id = data['episode_id']

        current_user_id = get_jwt_identity()

        if not Guest.query.get(guest_id):
            return {"error":"Guest not found"},404
        
        if not Episode.query.get(episode_id):
            return {"error":"Episode not found"}
        
        try:
            new_appearance = Appearance(
                rating=rating,
                guest_id = guest_id,
                episode_id = episode_id
            )
            db.session.add(new_appearance)
            db.session.commit()

            return {
                "id": new_appearance.id,
                "rating": new_appearance.rating,
                "guest_id": new_appearance.guest_id,
                "episode_id": new_appearance.episode_id,
                "created_by_user_id": current_user_id
            },201
        except Exception as e:
            return {"error":str(e)}


