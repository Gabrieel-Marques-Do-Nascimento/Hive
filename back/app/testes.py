from main import app, socketIo
from flask_socketio import SocketIO

app.config["TESTING"] = True
teste_client= socketIo.test_client(app)
teste_client.send("hello")
reseived = teste_client.get_received()
print(reseived)
