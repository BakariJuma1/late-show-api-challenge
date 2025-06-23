from server.extension import db

class Episode(db.Model):

    __tablename__ = "episodes"

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String,nullable=False)
    number = db.Column(db.Integer,nullable=False)

    # rship
    appearances = db.relationship('Appearance',back_populates='episode',cascade='all, delete')
   
