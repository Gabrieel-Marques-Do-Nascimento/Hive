from flask import Blueprint
from flask_socketio import emit, SocketIO, join_room, leave_room
from datetime import datetime
from Database.usuarios import Users, Messages, db

socket_bp = Blueprint("socket_pb", __name__)





def socket_register(socketio: SocketIO):

    @socketio.on("channel")
    def channel(data: dict):
        user = Users.query.filter_by(id=data["id"]).first()
        user.online = datetime.utcnow()
        d_user = Users.query.filter_by(id=data["d-id"]).first()

        msg_db = Messages(user=user, message=data["message"], pessoaId=data.get(
            "d-id"), senderId=data.get("id"))

        dest_msg_db = Messages(user=d_user, pessoaId=data.get(
            "d-id"), message=data.get("message"), senderId=data.get("id"))
        db.session.add(dest_msg_db)
        db.session.add(msg_db)
        db.session.commit()

        emit("channel", data, to=data["room"], broadcast=True)

    @socketio.on("join")
    def join(data):
        join_room(data["room"])
        emit("join", data["name"]+" (-_-)"+data["room"], broadcast=True)

    @socketio.on("leave")
    def leave(data):
        leave_room(data["room"])
        emit("leave", data["name"]+" (-_-)"+data["room"])

    @socketio.on('new-contact')
    def new_contact(data):
        user = Users.query.filter_by(id=data["id"]).first()
        if user:
        	emit(f"new-contact", {"message":"", "pessoa":user.id, "enviado":[], "online": None}, broadcast=True)
        else:
        	emit("error", {"message": "usuario nao encontrado"}, broadcast=True)
