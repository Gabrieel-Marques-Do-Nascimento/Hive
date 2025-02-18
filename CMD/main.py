from socketio import Client
import logging
import requests
import sys
import subprocess


token = {}


class Hive(Client):
    def __init__(self, url="http://127.0.0.1:5000", *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.url = url
        self.logguer = self._setup_logger()
        self.TextInput = "  HIVE>> "

    def _setup_logger(self) -> logging.Logger:
        """Configure logging for the client."""
        logger = logging.getLogger('  HIVE>> ')
        if not logger.handlers:
            handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def commands(self, data: str):
        """Execute commands based on user input."""
        if data == "help":
            self.logguer.info("""
                `help`: mostra essa mensagem
                `send:`: envia mensagem
                `resvd:`: mostra uma message recebida
                `login:`: faz login no servidor
                `exit`: sai do programa
                """)
        if data == "exit":
            sys.exit(0)

    def hive_input(self, data: str) -> str:
        return str(input(self.TextInput+data))

    def login(self):
        """Login to the Hive server."""
        user = self.hive_input(f"user: ")
        password = self.hive_input(f"password: ")
        reponce = requests.post(f"{self.url}/login",
                                json={"email": user, "password": password})
        httptoken = reponce.json().get("token")
        if httptoken:
            token['token'] = httptoken
            token['username'] = reponce.json().get('username')
            token['id'] = reponce.json().get('id')
            subprocess.run(['setx', "TOKEN", httptoken])

        return reponce

    def events(self):
        """Register event handlers."""
        @self.on("message_privada")
        def message(data):
            self.logguer(data)

    def hive_connec(self):
        """Connect to the Hive server and register event handlers."""
        self.connect(self.url)
        self.emit('registrar_usuario', {"id": 1})
        self.logguer.info("conectado")
        self.logguer.info(self.login().json())
        self.events()
        # self.wait()

    def hive_repl(self):
        while True:
            try:
                if not token:
                    self.login()
                    continue
                cmd = str(input("  HIVE>>"))
                self.commands(cmd)

            except Exception as err:
                self.logguer.error(f"erro: {err}")


if __name__ == "__main__":
    hive = Hive()
    hive.hive_connec()
    hive.hive_repl()
