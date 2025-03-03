import requests

reponce: requests.models.Response = requests.post(f"http://127.0.0.1:5000/login",
                                                          json={"email": "Gabriel", "password": "20211613"})
print(reponce.json())
data = reponce.json()

url = "http://127.0.0.1:5000" + "/my_msgs"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {data['token']}",
    "uid": str(data['id'])
}

try:
    response = requests.post(url,json={'id': data['id']}, headers=headers, timeout=4)

    # Diagnóstico
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # Tentando carregar JSON
    data = response.json()
    print("JSON Response:", data)

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
except requests.exceptions.JSONDecodeError as e:
    print("Erro ao decodificar JSON:", e)

