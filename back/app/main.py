from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import token_verify

import logging

# local
from Database import Users, Messages, db, data_str
from Rotas import users_blueprint, adm


app = Flask(__file__, static_folder='static')
CORS(app)
app.logger.setLevel(logging.INFO)

app.register_blueprint(users_blueprint)
app.register_blueprint(adm)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# -------------------------------------------------------------
# -------------------------------------------------------------
with app.app_context():
    db.create_all()


# gerenciador de msg
@app.route("/msg/<int:id>", methods=["POST"])
@token_verify
def gen(id):
    resp = request.get_json()
    app.logger.info(resp)
    return jsonify({"respost": "received"})




@app.route('/send_msg', methods=["POST"])
@token_verify
def send_msg(token):
    """
    camila: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk1NTU1NTUsInVpZCI6Mn0.Xd-9S0ar9WoThUGCS6fdjslc66htPMmFM06x_mZarQk
    
	gabriel: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk1NTUwOTIsInVpZCI6MX0.eu7tBI_lx42kYF_EdzQEQ2-qkEjZnSOON5YpA8cz_xc    
    
    curl -X POST "http://localhost:5000/send_msg" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk1NTU1NTUsInVpZCI6Mn0.Xd-9S0ar9WoThUGCS6fdjslc66htPMmFM06x_mZarQk" \
     -H "uid: 2" \
     -d '{
           "id": 2,
           "msg": "mensagem de teste",
           "P-id": 1
         }'
    
    """
    resp = request.get_json()
    id = resp["id"]
    msg = resp["msg"]
    dest_id = resp["P-id"]
    user = Users.query.filter_by(id=id).first()
    user.online = data_str
    msg_db = Messages(userId=id,pessoaId=dest_id, message=msg, is_my=True, senderId=id)
    d_msg_db = Messages(
    					userId=dest_id, message=msg,
    					pessoaId=id, senderId=id, is_my=False)
    db.session.add(msg_db)
    db.session.add(d_msg_db)
    db.session.commit()
    app.logger.info(resp)
    return jsonify({"respost": "received", "online":user.online}) 

@app.route('/my_msgs', methods=['POST'])
@token_verify
def mymesgs(token):
    """
    >>> Token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk0NDY5NDUsInVpZCI6MX0.NBKM_4OUNbcCTOpZKfTaE1qLG4CNNsnJ48IUh0iBY_I"
    
    curl -X POST http://localhost:5000/my_msgs \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk1NTUwOTIsInVpZCI6MX0.eu7tBI_lx42kYF_EdzQEQ2-qkEjZnSOON5YpA8cz_xc" \
     -H "uid: 1" \
     -d '{ "id": 1 }'
    """
    resp = request.get_json()
    id = resp["id"]
    user = Users.query.filter_by(id=id).first()
    db_msg = Messages.query.filter_by(userId=id)
    msg_all = db_msg.all()
    user.view = Messages.query.order_by(Messages.id.desc()).first().id
    db.session.commit()
    msgs = [{"message":msg.message, "pessoa":msg.pessoaId, "enviado":msg.senderId, "online": None} for msg in msg_all]
    return msgs






#@app.route("/")
#def index():
#    user_name = "Camila"
#    sender_name = "Gabriel"
#    return render_template("index.html", sender=sender_name, user=user_name,sensitive_data="er5543token554346")




#@app.route("/home")
#def home():
#    users = [{"username":"gabriel","time":"15:00","preview":"hello world"},{"username":"camila","time":"15:00","preview":"hello world"},{"username":"joao","time":"15:00","preview":"hello world"}]
#    return render_template("home.html", users= users, user="gau")




#@app.route("/login")
#def login():
#    return render_template("login.html")

# curl -X POST http://127.0.0.1:5000/msg/1 -H "Content-Type: application/json" -d '{"msg":"hello"}'

if __name__ == "__main__":
    app.run(debug=True)
