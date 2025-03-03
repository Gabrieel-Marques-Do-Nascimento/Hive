from flask import Blueprint, request
from flask_socketio import emit, SocketIO, join_room, leave_room
from datetime import datetime
from Database.cliente import Users, Messages, Contacts, db
from flask import Flask


socket_bp = Blueprint("socket_pb", __name__)

from .utils import setup_logger  # noqa: E402

socket_logger = setup_logger("socket_logger", log_file="socket.log")
socket_logger.info("SocketIO initialized")

ususarios_conectados = {}


def socket_register(socketio: SocketIO, app: Flask) -> None:
    """
    Register socket events for the application.

    Args:
        socketio (SocketIO): The SocketIO instance to register events on
    """
    def save_message(data_base: dict) -> bool:
        """
        Salva a mensagem no banco de dados

        Args:
            data_base (dict): Dados da mensagem
    >>> data_base: dict = {'destinatario_id': int, 'mensagem': str, 'id': int}
        """
        try:
            socket_logger.info(f"Saving message: {data_base}")
            user = Users.query.filter_by(id=data_base["id"]).first()
            user.online = datetime.utcnow()
            destinatario = Users.query.filter_by(
                id=data_base["destinatario_id"]).first()
            user_message = Messages(
                user=user, message=data_base["mensagem"], other_Id=data_base["destinatario_id"], to=data_base["destinatario_id"])
            destinatario_message = Messages(
                user=destinatario, message=data_base["mensagem"], other_Id=data_base["id"], to=data_base["destinatario_id"])
            db.session.add(destinatario_message)
            db.session.add(user_message)
            db.session.commit()

            return True
        except Exception as e:
            socket_logger.error("Erro ao salvar mensagem: %s", e)
            return False

    @socketio.on("connect")
    def connect():
        socket_logger.info("Cliente conectado")

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

        emit("channel", {
            "enviado": data.get("id"),
            "message": data.get("message"),
            "pessoa": data.get("d-id"),
            "online": None,
            "userid":  data.get("id")
        }, to=data["room"], broadcast=True)

    @socketio.on("registrar_usuario")
    def registrar_usuario(data):
        id = data["id"]
        ususarios_conectados[id] = request.sid
        socket_logger.info(
            f"Usuario {id} conectado com o socket {request.sid}")

    @socketio.on("send_message")
    def send_message(data):
        destinatario_id = int(data["destinatario_id"])
        mensagem = data["mensagem"]
        print(data)
        save_message(data)
        if destinatario_id in ususarios_conectados:
            destinatario_sid = ususarios_conectados[destinatario_id]
            socket_logger.info("message-enviada:" + mensagem)
            emit("message_privada", {
                 "mensagem": mensagem, "id": data["id"], "destinatario": destinatario_id}, to=destinatario_sid)
        else:
            emit("error", {"message": "Destinatário não encontrado"})

    @socketio.on('new-contact')
    def new_contact(data):
        try:
            print(data)
            constact = Users.query.filter_by(id=data["id"]).first()
            if constact and constact.id != data["userId"]:
                newConatact = Contacts(userId=data["userId"], contactId=constact.id,
                                       custom_name=data["custom_name"])
                db.session.add(newConatact)
                db.session.commit()
                socket_logger.info(f"User {constact.id} found")
                emit(f"new-contact", {"contact": constact.id,
                     "name": data["custom_name"]}, broadcast=True)

            else:
                emit(
                    "error", {"message": "usuario nao encontrado"}, broadcast=True)
        except Exception as e:
            socket_logger.critical(f"Error: {e}")
            emit("error", {"message": str(e)}, broadcast=True)

    @socketio.on('disconnect')
    def disconnect():
        socket_logger.info("Cliente desconectado")
        for user in ususarios_conectados:
            if ususarios_conectados[user] == request.sid:
                socket_logger.info(f"Usuario {user} desconectado")
                del ususarios_conectados[user]
                break
