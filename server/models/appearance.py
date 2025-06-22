from server.app import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.String,primary_key=False)
    rating = db.Column(db.Integer,nullable=False)

    guest_id = db.Column(db.Integer,db.ForeignKey('guests.id'),nullable=False)
    episode_id = db.Column(db.Integer,db.ForeignKey('episodes.id'),nullable=False)

    # make sure only 1-5 is accepted
    @validates('rating')
    def validate_ratin(self,key,value):
        if value <1 or value >5:
            raise ValueError('Rating must be between 1 and 5')
        return value