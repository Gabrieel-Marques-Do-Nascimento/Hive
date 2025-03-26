import os

import sqlite3
from utils import USER

with sqlite3.connect('hivy.db') as conn:
    cursor = conn.cursor()

    # Criando a tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            contact TEXT,
            update_time TEXT
        )
    ''')

    # Criando a tabela de mensagens
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            uid TEXT PRIMARY KEY,
            id TEXT,
            other_id TEXT,
            to_id TEXT,
            mid TEXT,
            message TEXT
        )
    ''')

    # Criando a tabela de login
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS login (
            uid TEXT PRIMARY KEY,
            token TEXT
        )
    ''')

    conn.commit()

class DB:
    def __init__(self, db_name='hivy.db'):
        self.db_name = db_name

    def connect(self):
        """Abre uma conexão com o banco de dados"""
        return sqlite3.connect(self.db_name)

    def all(self, table):
        """Retorna todos os registros de uma tabela"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()

class UserDB(DB):
    def __init__(self):
        super().__init__()
    #    with self.connect() as conn:
#            cursor = conn.cursor()
#            cursor.execute('''
#                CREATE TABLE IF NOT EXISTS users (
#                    id TEXT PRIMARY KEY,
#                    name TEXT,
#                    contact TEXT,
#                    update_time TEXT
#                )
#	        CREATE TABLE IF NOT EXISTS messages (
#	        				id TEXT,
#	        				other_id TEXT,
#	        				to TEXT,
#	        				mid TEXT,
#	        				message TEXT
#        CREATE TABLE IF NOT EXISTS login (
#        				token TEXT
#   
#            ''')
#            conn.commit()

    def create(self, user: USER):
        """Cria um novo usuário"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (id, name, contact, update_time) VALUES (?, ?, ?, ?)",
                           (user.user_id, user.name, user.contact, user.update))
            conn.commit()
        return True

    def select(self, user_id):
        """Busca um usuário pelo ID"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            return cursor.fetchone()

# As demais classes seguem a mesma lógica


class LoginDB(DB):
	def __init__(self):
		super().__init__()
#		with self.connect() as conn:
#				cursor = conn.cursor()
#				self.name: str = "login"
#				cursor.execute('''
#        CREATE TABLE IF NOT EXISTS login (
#        				token TEXT
#        )''')
#		conn.commit()
		
class MessagesDB(DB):
	def __init__(self):
		super().__init__()
#		with self.connect() as conn:
#				cursor = conn.cursor()
#				self.name: str = 'messages'
#				cursor.execute('''
#	        CREATE TABLE IF NOT EXISTS messages (
#	        				id TEXT,
#	        				other_id TEXT,
#	        				to TEXT,
#	        				mid TEXT,
#	        				message TEXT
#	        )''')
#		conn.commit()


class Tabels:
	users = "users"
	usersDB = UserDB()
	messges = "messages"
	messagesDB = UserDB()
	login = "login"
	loginDB = UserDB()
	


     
#	def All(self):
#	       self.cursor.execute("SELECT * FROM messages")
#	       return self.cursor.fetchall()




#if __name__ == '__main__':
#	import unittest
#	import os
#	from utils import USER
#	from your_module import UserDB  # Substitua "your_module" pelo nome do seu arquivo
#	
#	class TestUserDB(unittest.TestCase):
#	    def setUp(self):
#	        """Configuração inicial antes de cada teste"""
#	        self.test_db = 'test_hivy.db'
#	        self.user_db = UserDB()
#	        self.user_db.db_name = self.test_db  # Usar um banco de teste separado
#	
#	        # Criar um usuário fictício
#	        self.test_user = USER(user_id="123", name="Teste", contact="teste@email.com", update="2025-03-26")
#	
#	    def tearDown(self):
#	        """Executado após cada teste, remove o banco de dados"""
#	        if os.path.exists(self.test_db):
#	            os.remove(self.test_db)
#	
#	    def test_create_user(self):
#	        """Testa se o usuário é criado corretamente"""
#	        self.assertTrue(self.user_db.create(self.test_user))
#	
#	    def test_select_user(self):
#	        """Testa se um usuário pode ser buscado corretamente"""
#	        self.user_db.create(self.test_user)
#	        user = self.user_db.select("123")
#	
#	        self.assertIsNotNone(user)
#	        self.assertEqual(user[0], "123")  # ID
#	        self.assertEqual(user[1], "Teste")  # Nome
#	        self.assertEqual(user[2], "teste@email.com")  # Contato
#	        self.assertEqual(user[3], "2025-03-26")  # Update_time
#	
#	unittest.main()