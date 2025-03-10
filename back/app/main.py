from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from datetime import datetime

from auth import token_verify


# local
from Database import Users, Messages, Contacts, data_str
from Rotas import create_app, socketIo, app, db


# -------------------------------------------------------------
# -------------------------------------------------------------
with app.app_context():
    db.create_all()


@app.route('/my_msgs', methods=['POST'])
@token_verify
def mymesgs(token):
    """
    >>> Token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk0NDY5NDUsInVpZCI6MX0.NBKM_4OUNbcCTOpZKfTaE1qLG4CNNsnJ48IUh0iBY_I"

    curl -X POST http://localhost:5000/my_msgs \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk5MzQ5MTIsInVpZCI6MX0.6uk2tajbWL63judZYGyrsrsaMWbHe_xDxp74Y0KPQzc" \
     -H "uid: 1" \
     -d '{ "id": 1 }'
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
                        {"contact": contact.contact_Id, "name": contact.custom_name, 'created': contact.created_at,'update':  contact.update, 'id': contact.user.id})
        return jsonify([msgs, contacts])
    except AttributeError as e:
        app.logger.error(e)
        return ['erro']
    except Exception as e:
        app.logger.error(e)
        return jsonify([], [])  # ['erro']


if __name__ == "__main__":
    # app.run(debug=True)
    import os
    print(os.path.join(os.path.dirname(__file__), ""))
    socketIo.run(app, host="0.0.0.0")
