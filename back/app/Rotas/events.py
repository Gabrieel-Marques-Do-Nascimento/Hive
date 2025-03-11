from flask import Blueprint, request
from flask_socketio import emit, SocketIO, join_room, leave_room
from datetime import datetime
from Database.cliente import Users, Messages, Contacts, db
import auth
from flask import Flask


socket_bp = Blueprint("socket_pb", __name__)

from .utils import setup_logger  # noqa: E402

socket_logger = setup_logger("socket_logger", log_file="socket.log")
# socket_logger.info("SocketIO initialized")

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
            destinatario = Users.query.filter_by(
                id=data_base["to"]).first()
            user_message = Messages(
                user=user, message=data_base["message"], other_Id=data_base["to"], to=data_base["to"])
            destinatario_message = Messages(
                user=destinatario, message=data_base["message"], other_Id=data_base["id"], to=data_base["to"], created_at=datetime.now())
            db.session.add(destinatario_message)
            db.session.add(user_message)
            db.session.commit()

            return True
        except Exception as e:
            socket_logger.error("Erro ao salvar mensagem: %s", e)
            return False

    def status(user: Users, sid) -> bool:
        """
            Atualiza o status do usuário"
        """
        data_hora = datetime.now()
        print(data_hora)
        messages = Messages.query.filter(
            user.online < Messages.created_at, Messages.user_Id == user.id).all()
        print(messages)
        if len(messages) > 0:
            all_messages = [{
                "message": message.message, "id": message.user_Id, "to": message.to, "other_Id": message.other_Id, 'created': message.created_at.strftime("%d/%m/%Y %H:%M:%S")
            } for message in messages]
            print(all_messages)
            emit("status", {'status': 'atualizacoes',
                 'messages': all_messages}, to=sid)
        return True

    @socketio.on("contact-status")
    def contact_status(data):
        print(data)
        # if (data["contacts"], list):
        #     pass
        if data.get("id"):
            __status = 'online' if ususarios_conectados.get(data["id"]) else 'offline'
            socketio.emit("contact-status", {'status':__status}, to=ususarios_conectados[data["return"]])
        # online = []
        # for ct in data:
        #   if ususarios_conectados.get(ct):
        #       online.append(ct)

    @socketio.on("status")
    def _status(data):
        contacts_update = []
        for ct in data['contacts']:
            contact = Users.query.filter_by(
                user_Id=ct["id"], contact_Id=data["id"]).first()
            if contact.update > datetime.strptime(ct["update"], 'YYYY-MM-DD HH:MM:SS.ffffff'):
                contacts_update.append({"contact": contact.contact_Id, "name": contact.custom_name,
                                       'created': contact.created_at, 'update':  contact.update, 'id': contact.user.id})
            Contacts.query.filter_by(
                user_Id=ct["id"], contact_Id=data["contact"]).update(dict(update=datetime.now()))
        db.session.commit()
        emit("status", {'status': 'atualizacoes',
             'contacts': contacts_update}, to=request.sid)

    @socketio.on("connect")
    def connect():
        id = request.headers.get('id')
        if id is None:
            socket_logger.error("ID não encontrado")
            return
        socket_logger.info("Cliente conectado")
        ususarios_conectados[int(id)] = request.sid
        socket_logger.info(
            f"Usuario {id} conectado com o socket {request.sid}")
        user = Users.query.filter_by(id=id).first()
        status(user, request.sid)

    @socketio.on("bio")
    def b(data):
        print(data)
        id = int(data["id"])
        user = Users.query.filter_by(id=id).first()
        user.bio = data["bio"]
        user.update = datetime.now()
        db.session.commit()

    @socketio.on("send_message")
    def send_message(data):
        destinatario_id = int(data["to"])
        mensagem = data["message"]
        print(data)
        save_message(data)
        if destinatario_id in ususarios_conectados:
            destinatario_sid = ususarios_conectados[destinatario_id]
            socket_logger.info("message-enviada:" + mensagem)
            emit("message_privada", {
                "message": mensagem, "id": int(data["id"]), "to": int(destinatario_id), "other_Id": int(destinatario_id)
            }, to=destinatario_sid)
        else:
            emit("error", {
                "message": "Destinatário não encontrado"
            })

    @socketio.on('new-contact')
    def new_contact(data):
        try:
            print(data)
            user = Users.query.filter_by(id=int(data["userId"])).first()
            constact = Users.query.filter_by(id=int(data["id"])).first()
            if constact and constact.id != int(data["userId"]):
                newConatact = Contacts(user_Id=user.id, contact_Id=constact.id,
                                       custom_name=data["custom_name"])
                db.session.add(newConatact)
                db.session.commit()
                socket_logger.info(f"User {constact.id} found")
                emit(f"new-contact", {
                    "contact": constact.id,
                    "name": data["custom_name"]}, broadcast=True)

            else:
                emit(
                    "error", {
                        "message": "usuario nao encontrado"
                    }, broadcast=True)
        except Exception as e:
            socket_logger.critical(f"Error: {e}")
            emit("error", {
                "message": str(e)}, broadcast=True)

    @socketio.on('disconnect')
    def disconnect():
        socket_logger.info("Cliente desconectado")

        temp: dict = ususarios_conectados
        for key,  user in temp.items():
            if temp[key] == request.sid:
                socket_logger.info(f"Usuario {key}  desconectado")
                del ususarios_conectados[key]
                try:
                    dbuser = Users.query.filter_by(id=int(key)).first()
                    dbuser.online = datetime.now()
                    db.session.commit()
                except Exception as e:
                    socket_logger.error(f"Error: {e}")
                break
