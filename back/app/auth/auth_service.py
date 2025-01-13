from functools import wraps
from flask import jsonify, request
import jwt
from .JWT import token_crietor
from auth import jwt_config


def token_verify(function: callable) -> callable:
    """ Checking the valid Token and refreshing it. If not valid, return
        Info and stopping client request
        :parram - http request.headers: (Username / Token)
        :return - Json with the corresponding information.
    """
    @wraps(function)
    def decorated(*args, **kwargs):
        raw_token = request.headers.get('Authorization')
        uid = request.headers.get('uid')

        if not raw_token or not uid:
            return jsonify({"erro": "Nao Autorizado"}), 400
        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(
                token, key=jwt_config["TOKEN_KEY"], algorithms='HS256')
            token_uid = token_information["uid"]
            print(token_information)
        except jwt.InvalidSignatureError:
            return jsonify({"erro": "Token invalido"}), 401
        except jwt.ExpiredSignatureError:
            print("Token Expirado")
            return jsonify({"erro": "Token Expirado"}), 401
        except jwt.DecodeError as e:
            return jsonify({"erro": "Token invalido2"}), 401
        except KeyError as e:
            return jsonify({"erro": "Token invalido3"}), 401
        if uid and token_uid and int(token_uid) != int(uid):
            return jsonify({"erro": "user nao permitido"}), 400
        next_token = token_crietor.refesh(token)
        return function(next_token, *args, **kwargs)
    return decorated
