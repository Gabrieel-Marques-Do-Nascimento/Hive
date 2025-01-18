import sqlite3
from datetime import datetime

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect("sqlite3_db.db")
cursor = conn.cursor()

# Criar tabela Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    email_verify BOOLEAN DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

# Criar tabela Messages
cursor.execute("""
CREATE TABLE IF NOT EXISTS Messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    view BOOLEAN DEFAULT 0,
    FOREIGN KEY (userid) REFERENCES Users (id)
)
""")

# Função para inserir usuários
def add_user(username, password, email):
    try:
        cursor.execute("""
        INSERT INTO Users (username, password, email)
        VALUES (?, ?, ?)
        """, (username, password, email))
        conn.commit()
        print(f"Usuário {username} adicionado com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"Erro: {e}")

# Função para inserir mensagens
def add_message(userid, message):
    try:
        cursor.execute("""
        INSERT INTO Messages (userid, message)
        VALUES (?, ?)
        """, (userid, message))
        conn.commit()
        print(f"Mensagem adicionada com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"Erro: {e}")

# Função para listar usuários
def list_users():
    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)

# Função para listar mensagens
def list_messages():
    cursor.execute("""
    SELECT m.id, u.username, m.message, m.created_at, m.view
    FROM Messages m
    INNER JOIN Users u ON m.userid = u.id
    """)
    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
	# Inserir exemplo
	add_user("usuario1", "senha123", "usuario1@email.com")
	add_message(1, "Olá, esta é uma mensagem de teste!")
	
	# Listar conteúdo
	print("\nUsuários cadastrados:")
	list_users()
	
	print("\nMensagens registradas:")
	list_messages()
	
	# Fechar conexão
	conn.close()
	
	

"""

Detalhes e Explicações:

1. Banco de Dados SQLite:

O arquivo sqlite3_db.db será criado na mesma pasta do script, caso ainda não exista.

Use CREATE TABLE IF NOT EXISTS para evitar recriar tabelas.



2. Campo created_at:

O SQLite aceita o uso de CURRENT_TIMESTAMP para campos do tipo TEXT ou DATETIME.



3. Relacionamento (FOREIGN KEY):

A tabela Messages possui uma chave estrangeira (userid) que referencia a tabela Users.



4. Funções:

São criadas funções auxiliares para adicionar e listar usuários e mensagens.



5. Erro de Integridade:

O uso de sqlite3.IntegrityError captura problemas como tentativa de inserir valores duplicados em campos UNIQUE (ex.: username ou email).





---

Como Executar:

1. Salve o código em um arquivo Python (ex.: app.py).


2. Execute o script:

python app.py


3. Verifique o arquivo database.db para confirmar que os dados foram salvos corretamente.



Saída Esperada:

Usuário usuario1 adicionado com sucesso!
Mensagem adicionada com sucesso!

Usuários cadastrados:
(1, 'usuario1', 'senha123', 'usuario1@email.com', 0, '2025-01-13 12:00:00')

Mensagens registradas:
(1, 'usuario1', 'Olá, esta é uma mensagem de teste!', '2025-01-13 12:01:00', 0)


"""