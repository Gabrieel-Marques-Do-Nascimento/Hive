import socketio

# Cliente SocketIO
sio = socketio.Client()

# Evento de conexão
@sio.event
def connect():
    print("Conectado ao servidor!")

# Evento de desconexão
@sio.event
def disconnect():
    print("Desconectado do servidor!")

# Manipulador para o canal de mensagens
@sio.on("channel")
def on_message(data):
    print(f"Nova mensagem recebida: {data}")

# Manipulador para o evento de novo contato
@sio.on("new-contact")
def on_new_contact(data):
    print(f"Novo contato adicionado: {data}")

# Manipulador para erros
@sio.on("error")
def on_error(data):
    print(f"Erro recebido: {data}")

# Conectar ao servidor SocketIO
sio.connect("http://localhost:5000")  # Alterar para o endereço do seu servidor

# Função para enviar uma mensagem
def enviar_mensagem(room, user_id, destinatario_id, mensagem):
    sio.emit("channel", {
        "room": room,
        "id": user_id,
        "d-id": destinatario_id,
        "message": mensagem
    })

# Função para entrar em uma sala
def entrar_sala(room, nome_usuario):
    sio.emit("join", {
        "room": room,
        "name": nome_usuario
    })

# Função para sair de uma sala
def sair_sala(room, nome_usuario):
    sio.emit("leave", {
        "room": room,
        "name": nome_usuario
    })

# Função para adicionar um novo contato
def adicionar_contato(user_id):
    sio.emit("new-contact", {
        "id": user_id
    })

# Exemplo de uso
if __name__ == "__main__":
    entrar_sala("sala123", "Alice")
    enviar_mensagem("sala123", user_id=1, destinatario_id=2, mensagem="Olá, tudo bem?")
    adicionar_contato(2)
    sair_sala("sala123", "Alice")

    # Manter o cliente ativo
    sio.wait()
