from .users import users_blueprint
from .adm import adm
from flask_socketio import  SocketIO
from .events import socket_register, socket_bp

from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging


socketIo = SocketIO(cors_allowed_origins="*")


def create_app():
		app = Flask(__file__, static_folder='static')
		CORS(app)
		
		app.config["SECRET"] = "secret"
		socketIo.init_app(app)
		app.logger.setLevel(logging.INFO)
		socket_register(socketIo)
		app.register_blueprint(users_blueprint)
		app.register_blueprint(adm)
		app.register_blueprint(socket_bp)
		
		
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
		app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
		app.config["DEBUG"] = True
		return app
