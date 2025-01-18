from flask import Blueprint
# autenticacao
from auth import token_verify


adm = Blueprint("ADM", __name__)

