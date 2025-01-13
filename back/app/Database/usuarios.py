from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# configuração do banco de dados
db = SQLAlchemy()

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
    created_at = db.Column(
        db.String(20), default=data_str)

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Messages(db.Model):
    id = db.Column(
        db.Integer, primary_key=True)
    userid = db.Column(
        db.Integer, nullable=False)
    message = db.Column(
        db.String(200), nullable=False)
    created_at = db.Column(
        db.String(20), default=data_str)