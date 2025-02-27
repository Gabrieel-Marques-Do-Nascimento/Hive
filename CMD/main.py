from socketio import Client
import logging
import requests
import sys
import subprocess
import platform


token = {}


"""
exemplo de login:

{'id': 1, 'message': 'Login bem-sucedido!', 'status': 'ok', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI0Njg3ODYsInVpZCI6MX0.X98ymRJsSMFczgqwvdnEHZnsH9U5fWV06MzAaLjph20', 'token_name': '1463token-as-savekjg', 'username': 'Gabriel'}


"""


class Hive(Client):
    def __init__(self, url="http://127.0.0.1:5000", *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.url = url
        self.logguer = self._setup_logger()
        self.TextInput = "  HIVE>> "
        self.channel = None
        self.command_txt = ''

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
        match data:
            case "help":
                self.logguer.info("""
                `help`: mostra essa mensagem
                  pv=id : conectar com amigo
                `send:`: envia mensagem
                `resvd:`: mostra uma message recebida
                `login:`: faz login no servidor
                `exit`: sai do programa
                """)
            case "exit":
                if self.channel:
                    self.channel = None
                    self.command_txt = ''
                    return 'saindo do canal'
                self.logguer.info("saindo...")
                sys.exit(0)
            # case pv:
            #     freendId = data.split("=")[1]
            #     return 'exit', f"conectando com {freendId}..."
            case _:
                if data.startswith('pv='):
                    print(data.split("="))
                    freendId = data.split("=")[1]
                    self.channel = freendId
                    self.command_txt = f"pv={freendId}"
                    return f"conectando com {freendId}..."
                return '', "comando não encontrado"
        return data, ""

    def hive_input(self, data: str) -> str:
        return str(input(self.TextInput+data))

    def login(self):
        """Login to the Hive server."""
        user = self.hive_input(f"user: ")
        password = self.hive_input(f"password: ")
        if not user or not password:
            user = "Gabriel"
            password = "20211613"
        reponce = requests.post(f"{self.url}/login",
                                json={"email": user, "password": password})
        httptoken = reponce.json().get("token")
        if httptoken:
            token['token'] = httptoken
            token['username'] = reponce.json().get('username')
            token['id'] = reponce.json().get('id')
            if platform.system() == "windows":
                subprocess.run(['setx', "TOKEN", httptoken])
            if platform.system() == "linux":
                pass

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
                cmd = self.hive_input(self.command_txt + ': ' if self.channel else '')
                if not self.channel or cmd == "exit":
                    self.logger.info(cmd)
                    result = self.commands(cmd)
                    continue
                if self.channel:
                    self.emit("send_message", {"mensagem": cmd, 'destinatario_id': self.channel})
                    continue


            except Exception as err:
                self.logguer.error(f"erro: {err}")


if __name__ == "__main__":
    hive = Hive()
    hive.hive_connec()
    hive.hive_repl()
