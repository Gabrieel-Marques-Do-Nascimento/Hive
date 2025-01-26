from flask import  Blueprint
from flask_socketio import emit, SocketIO

socket_bp = Blueprint("socket_pb",__name__)

def socket_register(socketio: SocketIO):
	@socketio.on("")