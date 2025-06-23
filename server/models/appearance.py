from server.extension import db
from sqlalchemy.orm import validates

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    rating = db.Column(db.Integer,nullable=False)

    guest_id = db.Column(db.Integer,db.ForeignKey('guests.id'),nullable=False)
    episode_id = db.Column(db.Integer,db.ForeignKey('episodes.id'),nullable=False)

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')


    # make sure only 1-5 is accepted
    @validates('rating')
    def validate_ratin(self,key,value):
        if value <1 or value >5:
            raise ValueError('Rating must be between 1 and 5')
        return value