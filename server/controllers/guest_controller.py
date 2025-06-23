from flask_restful import Resource
from server.models.guest import Guest

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return [
            {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
            for guest in guests
        ], 200
