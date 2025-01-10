from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging




app = Flask(__file__)
CORS(app)
app.logger.setLevel(logging.INFO)


# configuração do banco de dados
db = SQLAlchemy()

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


# curl -X POST http://127.0.0.1:5000/msg/1 -H "Content-Type: application/json" -d '{"msg":"hello"}'
if __name__ == "__main__":
    app.run(debug=True)
