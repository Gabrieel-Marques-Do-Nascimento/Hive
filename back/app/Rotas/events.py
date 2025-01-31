from flask import Blueprint
from flask_socketio import emit, SocketIO, join_room, leave_room
from datetime import datetime
from Database.usuarios import Users, Messages, db

socket_bp = Blueprint("socket_pb", __name__)


def socket_register(socketio: SocketIO):

    @socketio.on("channel")
    def channel(data: dict):

        #    msg_db = Messages(user=user, pessoaId=dest_id, message=msg, senderId=id)
        #     d_msg_db = Messages(
        #         user=dest_user, message=msg,
        #         pessoaId=id, senderId=id
        #     )

        user = Users.query.filter_by(id=data["id"]).first()
        user.online = datetime.utcnow()
        d_user = Users.query.filter_by(id=data["d-id"]).first()

        msg_db = Messages(user=user, message=data["message"], pessoaId=data.get(
            "d-id"), senderId=data.get("id"))

        dest_msg_db = Messages(user=d_user, pessoaId=data.get(
            "id"), message=data.get("message"), senderId=data.get("id"))
        db.session.add(dest_msg_db)
        db.session.add(msg_db)
        db.session.commit()

        emit("channel", data, to=data["room"], broadcast=True)

    @socketio.on("join")
    def join(data):
        join_room(data["room"])
        emit("join", data["name"]+" (-_-)"+data["room"])

    @socketio.on("leave")
    def leave(data):
        leave_room(data["room"])
        emit("leave", data["name"]+" (-_-)"+data["room"])

    @socketio.on('new-contact')
    def new_contact(data):
        pass
