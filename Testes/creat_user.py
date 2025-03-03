"""
USERS DE TESTE:.
id 1:
	{'username':"Gabriel", "password": "20211613", "email": "gabriel@email.com.br"}
id 2:
	'username':"Camila", "password": "20211613", "email": "camila@email.com.br"}
	
id 3:
	Pedro'


"""

usersTest = [
				{'username':"Gabriel", "password": "20211613", "email": "gabriel@email.com.br"},
				{'username':"Camila", "password": "20211613", "email": "camila@email.com.br"},
				{'username':"Pedro", "password": "20211613", "email": "pedro@email.com.br"},
				{'username':"Ana-livia", "password": "20211613", "email": "ana-livia@email.com.br"},
				{'username':"Joao", "password": "20211613", "email": "joao@email.com.br"},
				{'username':"Jose", "password": "20211613", "email": "jose@email.com.br"}
					]




import  requests
from time import  sleep

url = "http://127.0.0.1:5000"

resp = requests.post(url + "/create", json={'username':"Pedro", "password": "20211613", "email": "pedro@email.com.br"})

#resp = requests.post(url+"/login", json={'username':"Gabriel", "password": "20211613"})


print(resp.text)



"""
curl -X POST http://localhost:5000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "Gabriel",  "password": "20211613"}'

""" 