from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# configuração do banco de dados
db = SQLAlchemy()

data_str = datetime.strftime(datetime.now(),   "%d %m %Y %H:%M")
data_objt = datetime.strptime(data_str,   "%d %m %Y %H:%M")


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    email_verify = db.Column(db.Boolean, default=False)
    # substituir por uma forma de armazenar no channel do user, is online
    # reducao de consumo de cpu
    online = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    view = db.Column(db.Integer, default=0)

    # Relacionamento com Messages
    messages = db.relationship('Messages', backref='user', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Messages(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"),
                       nullable=False)  # Chave estrangeira para Users
    senderId = db.Column(db.Integer, nullable=True)
    pessoa = db.Column(db.String(200))
    pessoaId = db.Column(db.Integer)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Mensagem {self.id}>'


class Contacts(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"),
                       nullable=False)  # Chave estrangeira para Users
    contactId = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)  # Chave estrangeira para Users
    custom_name = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


if __name__ == "__main__":
    pass
# # Criar um novo usuário
# novo_usuario = Users(username="Joao", password="senha123", email="joao@email.com")
#
# # Criar uma mensagem associada ao usuário
# mensagem = Messages(user=novo_usuario, message="Olá, mundo!")
#
# # Adicionar ao banco de dados
# db.session.add(novo_usuario)
# db.session.add(mensagem)
# db.session.commit()

# acessar a mensagem de um usuario
# usuario = Users.query.filter_by(username="Joao").first()
# for mensagem in usuario.messages:
#    print(mensagem.message)

# acessar uma mensagem
# mensagem = Messages.query.first()
# print(mensagem.user.username)
