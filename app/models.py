import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=False)
    score = db.Column(db.Integer, index=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, nickname, score):
        self.nickname       = nickname
        self.score          = score

    def __repr__(self):
        return '<User %r>' % (self.nickname)