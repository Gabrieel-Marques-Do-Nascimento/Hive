"""
USERS DE TESTE:.
id 1:
	{'username':"Gabriel", "password": "20211613", "email": "gabriel@email.com.br"}
id 2:
	'username':"Camila", "password": "20211613", "email": "camila@email.com.br"}
	
id 3:
	Pedro'


"""

import  requests

url = "http://127.0.0.1:5000"

resp = requests.post(url + "/create", json={'username':"Pedro", "password": "20211613", "email": "pedro@email.com.br"})

#resp = requests.post(url+"/login", json={'username':"Gabriel", "password": "20211613"})


print(resp.text)



"""
curl -X POST http://localhost:5000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "Gabriel",  "password": "20211613"}'

""" 