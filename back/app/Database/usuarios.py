from app import db
from datetime import datetime


data_str = datetime.strftime(datetime.now(),   "%d %m %Y %H:%M")
data_objt = datetime.strptime(data_str,   "%d %m %Y %H:%M")


class Users(db.Model):
    id = db.Column(
        db.Integer, primary_key=True)
    username = db.Column(
        db.String(80), unique=True, nullable=False)
    password = db.Column(
        db.String(200), nullable=False)
    email = db.Column(
        db.String(200), unique=True, nullable=False)
    email_verify = db.Column(db.Boolean, default=False)
    permision = db.Column(db.String(80), default="base")
    created_at = db.Column(
        db.String(20), default=data_str)

    def __repr__(self):
        return f'<Usuario {self.username}>'
