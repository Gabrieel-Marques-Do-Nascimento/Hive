from flask import  Blueprint
from flask_socketio import emit, SocketIO, join_room, leave_room

socket_bp = Blueprint("socket_pb",__name__)

def socket_register(socketio: SocketIO):
	
	@socketio.on("channel")
	def channel(data):
		emit("channel", data, to=data["room"], broadcast=True)
	
	@socketio.on("join")
	def join(data):
		join_room(data["room"])
		emit("join", data["name"]+" (-_-)"+data["room"])

	@socketio.on("leave")
	def leave(data):
		leave_room(data["room"])
		emit("leave", data["name"]+" (-_-)"+data["room"])