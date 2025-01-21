from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# configuração do banco de dados
db = SQLAlchemy()

data_str = datetime.strftime(datetime.now(),   "%d %m %Y %H:%M")
data_objt = datetime.strptime(data_str,   "%d %m %Y %H:%M")


class Users(db.Model):
    __tablename__ = "Users"
    
    id = db.Column(
        db.Integer, primary_key=True)
    username = db.Column(
        db.String(80), unique=True, nullable=False)
    password = db.Column(
        db.String(200), nullable=False)
    email = db.Column(
        db.String(200), unique=True, nullable=False)
    email_verify = db.Column(db.Boolean, default=False)
    online = db.Column(db.String(20), default=data_str)
    created_at = db.Column(
        db.String(20), default=data_str)
    view = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Usuario {self.username}>'


class Messages(db.Model):
    id = db.Column(
        db.Integer, primary_key=True)
    userId = db.Column(
        db.Integer, db.ForeignKey("Users.id"))
    senderId = db.Column(
        db.Integer)
    online = db.Column(db.String(20))
    pessoa = db.Column(
    db.String(200))
    
    pessoaId = db.Column(
    	db.Integer)
    message = db.Column(
        db.String(200), nullable=False)
    created_at = db.Column(
        db.String(20), default=data_str)
    
    is_my = db.Column(
        db.Boolean, default=False)
    def __repr__(self):
        return f'<Usuario {self.id}>'


if __name__ == "__main__":
    # novo user
    novo_usuario = Users(
        username="Gabriel",
        password='20211613',
        email='gabriel@gmail.com'
    )
    db.session.add(novo_usuario)
    db.session.commit()
    print(f'Usuário criado: {novo_usuario}')
	# consultar todos users
    usuarios = Users.query.all()
    for usuario in usuarios:
        print(f'Usuário: {usuario.username}, Email: {usuario.email}')
	# auterar campo do user
#    usuario = Users.query.filter_by(username='usuario123').first()
#    if usuario:
#        usuario.email_verify = True
#        usuario.online = datetime.strftime(datetime.now(), "%d %m %Y %H:%M")
#        db.session.commit()
#        print(f'Informações atualizadas: {usuario}')
#    else:
#        print('Usuário não encontrado.')
#    # deletar user
#    usuario = Users.query.filter_by(username='usuario123').first()
#    if usuario:
#        db.session.delete(usuario)
#        db.session.commit()
#        print(f'Usuário {usuario.username} deletado com sucesso.')
#    else:
#        print('Usuário não encontrado.')        