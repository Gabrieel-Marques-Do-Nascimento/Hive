import logging
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

import os
from auth.JWT_C import token_update
from Database.usuarios import Users, Messages, db


users_blueprint = Blueprint('users', __name__)


# # Configuração do logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # Criar um manipulador de arquivo
# handler = logging.FileHandler('users.log')
# handler.setLevel(logging.INFO)

# # Definir o formato do log
# formatter = logging.Formatter(
#     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)

# # Adicionar o manipulador ao logger
# logger.addHandler(handler)


@users_blueprint.route('/create', methods=['POST'])
def create_user():
    """ create user 
>>> http://127.0.0.1:5000/create # url

>>> {"username": "BIEL2", "password": "Gabrielm02$", "email":"biupjl@gmail.com"} # json


curl -X POST http://localhost:5000/create \
     -H "Content-Type: application/json" \
     -d '{"username": "Gabriel", "password": "20211613", "email":"gabriel@gmail.com"}'
   """

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    hash_password = generate_password_hash(password)
    new_user = Users(username=username, password=hash_password, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso!','token': token_update.creat(new_user.id),"id":new_user.id, 'token_name': '1463token-as-savekjg', 'status': 'ok'})


@users_blueprint.route('/login', methods=['POST'])
def login():
    """ login user
    http://127.0.0.1:5000/login # url
    >>> {"username": "BIEL2", "password": "Gabrielm02$"} # json
    
    curl -X POST http://localhost:5000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "Gabriel",  "password": "20211613"}'
    """
    data = request.get_json()

    username = data.get('email')
    password = data.get('password')
    if '@' in username:
        user = Users.query.filter_by(email=username).first()
    else:
        user = Users.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login bem-sucedido!', 'token': token_update.creat(user.id),"id":user.id, 'token_name': '1463token-as-savekjg', 'status': 'ok'})
    return jsonify({'message': 'Credenciais inválidas!', 'status': 'error'})


#@users_blueprint.route('/login-page', methods=['GET'])
#def login_page():
#    """ login page"""
#    return render_template('login.html')


@users_blueprint.route("/teste")
def info():
	"""
	curl -X GET http://localhost:5000/teste
	"""
	return jsonify({"users":[{"id":user.id, "name":user.username, "email":user.email, "online":user.online, "vew":user.view} for user in Users.query.all()]})
