from socketio import Client
import logging
import requests
import sys
import subprocess
import platform
from threading import Thread 
from time import  sleep
from rich import  print
from rich.console import  Console


console = Console

token: dict = {}


"""
exemplo de login:

{'id': 1, 'message': 'Login bem-sucedido!', 'status': 'ok', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDI0Njg3ODYsInVpZCI6MX0.X98ymRJsSMFczgqwvdnEHZnsH9U5fWV06MzAaLjph20', 'token_name': '1463token-as-savekjg', 'username': 'Gabriel'}


"""


class Hive(Client):
    def __init__(self, url="http://127.0.0.1:5000", *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.url: str= url
        self.logguer = self._setup_logger()
        self.TextInput: str = "  HIVE>> "
        self.channel: str | None= None
        self.command_txt: str = ''
        self.server_login: str = ""
        self.userId: int= 1

    def _setup_logger(self) -> logging.Logger:
        """Configure logging for the client."""
        logger: logging.Logger = logging.getLogger('  HIVE>> ')
        if not logger.handlers:
            handler : logging.StreamHandler= logging.StreamHandler()
        formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def commands(self, data: str):
        """Execute commands based on user input."""
        match data:
            case "help":
                print("""
                `help`: mostra essa mensagem
                  chl=id : conectar com amigo
                `send:`: envia mensagem
                `contacts`: exibe uma lista de contatos
                `add`: adiciona um novo contato
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
                if data.startswith('chl=') and not data.endswith(str(self.userId)):
                    print(data.split("="))
                    freendId: str = data.split("=")[1]
                    self.channel: str= freendId
                    self.command_txt = f"channel[ {freendId} ]"
                    return f"conectando com {freendId}..."
                return '', "comando não encontrado"
        return data, ""

    def hive_input(self, data: str) -> str:
        print(f"[bold red]{self.TextInput+data}[/bold red]", end="")
        return str(input())

    def login(self):
        """Login to the Hive server."""
        
        user: str = self.hive_input(f"user: ")
        password:str = self.hive_input(f"password: ")
        if not user or not password:
            user = "Gabriel"
            password = "20211613"
        reponce: requests.models.Response = requests.post(f"{self.url}/login",
                                json={"email": user, "password": password})
        self.server_login: dict= reponce.json()
        self.userId = self.server_login["id"]
        self.emit('registrar_usuario', {"id": self.userId})
        httptoken: str = reponce.json().get("token")
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
            print(self.server_login)
            print(f"channel[{data['id']}]:{data['mensagem']}")
            if not self.channel:
            	print(f"caso deseje responder use o command `chl={data['id']}`")
            print(f"\n{self.TextInput}",end="")
            	

    def hive_connec(self):
        """Connect to the Hive server and register event handlers."""
        self.connect(self.url)
        self.logguer.info("conectado")
        #self.logguer.info(self.login().json())
        Thread(target=self.events).start()
        # self.wait()

    def hive_repl(self):
        while True:
            try:
                if not token:
                    sleep(1)
                    self.login()
                    continue
                cmd: str  = self.hive_input(self.command_txt + ': ' if self.channel else '')
                if not self.channel or cmd == "exit":
                    self.logger.info(cmd)
                    result: str | None | list = self.commands(cmd)
                    continue
                if self.channel:
                    self.emit("send_message", {"mensagem": cmd, 'destinatario_id': self.channel, "id": self.userId})
                    continue


            except Exception as err:
                self.logguer.error(f"erro: {err}")




if __name__ == "__main__":
    hive: Hive = Hive()
    def events():
    	hive.hive_connec()
    Thread(target=events).start()
    hive.hive_repl()
