from flask import request, jsonify
from auth import token_verify

from Database import Users
from Rotas import create_app, socketIo, app, db

with app.app_context():
    db.create_all()


@app.route('/my_msgs', methods=['POST'])
@token_verify
def mymesgs(token):
    """
 Retorna as mensagens do usuário autenticado.
    """
    try:
        resp = request.get_json()
        id = resp.get("id")  # Evita KeyError se "id" não existir
        if id is None:
            return jsonify({"error": "ID não fornecido"}), 400
        user = Users.query.filter_by(id=id).first()
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        app.logger.info(resp)
        msgs = []
        contacts = []
        if user and user.messages:
            for mensage in user.messages:
                if mensage:
                    msgs.append({"message": mensage.message, "other_Id": mensage.other_Id,
                                 "to": mensage.to, "id": user.id})
        if not user or not user.messages:
            msgs = []
        if user and user.contacts:
            for contact in user.contacts:
                if contact:
                    contacts.append(
                        {"contact": contact.contact_Id, "name": contact.custom_name, 'created': contact.created_at, 'update':  contact.update, 'id': contact.user.id})
        return jsonify([msgs, contacts])
    except AttributeError as e:
        app.logger.error(e)
        return jsonify([], [])  # ['erro']
    except Exception as e:
        app.logger.error(e)
        return jsonify([], [])  # ['erro']


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT"))
    socketIo.run(app, host="0.0.0.0", port=port, allow_unsafe_werkzeug=True)
