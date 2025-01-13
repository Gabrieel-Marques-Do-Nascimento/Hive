from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import logging

# local
from Database import Users, Messages, db
from Rotas import users_blueprint


app = Flask(__file__, static_folder='static')
CORS(app)
app.logger.setLevel(logging.INFO)

app.register_blueprint(users_blueprint)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# -------------------------------------------------------------
# -------------------------------------------------------------
with app.app_context():
    db.create_all()


# gerenciador de msg
@app.route("/msg/<int:id>", methods=["POST"])
def gen(id):
    resp = request.get_json()
    app.logger.info(resp)
    return jsonify({"respost": "received"})




@app.route('send_msg', methods=["POST"])
def send_msg():
    resp = request.get_json()
    app.logger.info(resp)
    return jsonify({"respost": "received"}) 

@app.route('/my_msgs', methods=['POST'])
def mymesgs():
    resp = request.get_json()
    lista_msgs: list = []
    return lista_msgs






@app.route("/")
def index():
    user_name = "Camila"
    sender_name = "Gabriel"
    return render_template("index.html", sender=sender_name, user=user_name,sensitive_data="er5543token554346")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")

# curl -X POST http://127.0.0.1:5000/msg/1 -H "Content-Type: application/json" -d '{"msg":"hello"}'
if __name__ == "__main__":
    app.run(debug=True)
