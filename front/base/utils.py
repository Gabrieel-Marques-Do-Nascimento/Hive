

class USER:
    def __init__(self, user):
        self.user: dict = user
        self.id: int = user["contact"]
        self.name: str = user["name"]
        self.update: str = user["update"]
        self.null: str = "null"
        self.user_id: int = user["id"]


class BaseName:
	name = "base"
	up = "up"
	down = "down"
	left = "left"
	right = "right"


class Requestist:
    def __init__(self):
        import requests
        self.request = requests
        self.url = "http://127.0.0.1:5000"
        self.headers = {"Content-Type": "application/json"}
        self.data = {}
        self.response = {}
        self.status_code = 0
        self.json = {}
    
    def login(self, data: dict):
        self.data = data

        self.response = self.request.post(
            f"{self.url}/login",
            headers=self.headers,
            json=self.data,
        )
        self.status_code = self.response.status_code
        self.json = self.response.json()
        return self.response
     