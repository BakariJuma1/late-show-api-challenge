from server.app import db

class Guest(db.Model):
    __tablename__ = 'guests'
    name = db.Column(db.String,nullable=False)
    occupation = db.Column(db.String,nullable=False)

    # rship
    appearances = db.relationship('Appearance',backref='guest',cascade='all,delete')
