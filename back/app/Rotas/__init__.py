from .users import users_blueprint
from flask_socketio import SocketIO
from .events import socket_register, socket_bp

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging


from Database import db


socketIo = SocketIO(cors_allowed_origins="*", async_mode="gevent")


def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)

    app.config["SECRET"] = "secret"
    socketIo.init_app(app)
    app.logger.setLevel(logging.INFO)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(socket_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["DEBUG"] = True
    db.init_app(app)
    socket_register(socketio=socketIo, app=app)
    return app


app = create_app()
# CORS(app, origins=["http://127.0.0.1:8081"])
CORS(app, supports_credentials=True)
