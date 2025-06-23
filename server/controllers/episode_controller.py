from flask_restful import Resource
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.extension import db
from flask import jsonify
from server.models.appearance import Appearance


class DeleteEpisode(Resource):
    @jwt_required()
    def delete(self,id):
        episode =Episode.query.get(id)
        if not episode:
            return {"error":"Episode not found"},404
        
        db.session.delete(episode)
        db.session.commit()

        return {"message":f"Episode{id} deleted succesfully"},200
    
class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return   [
            {
                "id": ep.id,
                "date": ep.date,
                "number": ep.number 
            }
            for ep in episodes
        ] ,200
    
class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        return {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [
                {
                    "id": a.id,
                    "rating": a.rating,
                    "guest": {
                        "id": a.guest.id,
                        "name": a.guest.name,
                        "occupation": a.guest.occupation
                    }
                }
                for a in episode.appearances
            ]
        }, 200
