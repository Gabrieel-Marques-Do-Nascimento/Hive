from flask import  Flask, request, jsonify
from flask_cors import CORS
import logging




app = Flask(__file__)
CORS(app)
app.logger.setLevel(logging.INFO)


# gerenciador de msg
@app.route("/msg/<int:id>", methods=["POST"])
def gen(id):
	resp = request.get_json()
	app.logger.info(resp)
	return jsonify({"respost":"received"})
	


# curl -X POST http://127.0.0.1:5000/msg/1 -H "Content-Type: application/json" -d '{"msg":"hello"}'

if __name__ == "__main__":
	app.run(debug=True)