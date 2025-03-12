from main import app, socketIo
from flask_socketio import SocketIO
import pytest
import requests
from time import sleep

@pytest.fixture 
def socketio_client():
    app.config['TESTING'] = True
    test_client = socketIo.test_client(app)
    return test_client

def create_user_test():
    resp = requests.post('http://http://127.0.0.1:5000/create',json={'username':"Teste", "password": "teste", "email": "teste@email.com.br"})
    assert resp.status_code == 200
    assert resp.json() == {'message': 'User created successfully'}

def login_user_test():
    resp = requests.post('http://http://127.0.0.1:5000/login',json={'username':"Teste", "password": "teste"})
    assert resp.status_code == 200
    assert resp.json() == {'message': 'Login bem-sucedido!'}


def teste_message_socket(socketio_client):
    create_user_test()
    sleep(1)
    login_user_test()
    socketio_client.emit('send_message', {'message': 'Hello, world!','to':1,'id':7, 'other_Id':1})
    assert socketio_client.get_received() == [{'name': 'erro', 'args': [{'message': 'Hello, world!'}]}]