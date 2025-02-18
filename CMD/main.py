from socketio import Client
import logging




class Hive(Client):
	def __init__(self, url="http://127.0.0.1:5000", *args, **Kwargs):
		super().__init__(*args, **Kwargs)
		self.url = url
		self.logguer = self._setup_logger()
		
		
	def _setup_logger(self) -> logging.Logger:
	       """Configure logging for the client."""
	       logger = logging.getLogger(__name__)
	       if not logger.handlers:
	       	handler = logging.StreamHandler()
	       formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s')
	       handler.setFormatter(formatter)
	       logger.addHandler(handler)
	       logger.setLevel(logging.INFO)
	       return logger
	def events(self):
	       @self.on("message_privada")
	       def message(data):
	       	self.logguer(data)
	       
	def hive_connec(self):
		self.connect(self.url)
		self.logguer.info("conectado")
		#self.wait()
	
	def hive_repl(self):
		while True:
			try:
				cmd = str(input("  HIVE>>"))
				
			except Exception as err:
				self.logguer.error(f"erro: {err}")



if __name__ == "__main__":
	hive = Hive()
	hive.hive_connec()
	hive.hive_repl()