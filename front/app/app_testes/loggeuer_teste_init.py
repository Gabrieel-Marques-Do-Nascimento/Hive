import logging
import time
import  os
from datetime import datetime


class ActivationTime:
	def __init__(self):
		self.init_time = time.time()
		self.cont = 1
		self.__file_name="logguer"
		self.sum = 0

	def file_name(self, name, filetimename=False):
		self.__file_name = name + datetime.now().strftime("%Y-%m-%d %H-%M-%S") if filetimename else name
		
		
		
	def clear(self):
		file_name = os.path.join(os.path.dirname(__file__), self.__file_name + ".log")
		print("&&" ,file_name)
		with open(file_name, "w") as file:
			file.write("")
	
	def file_logguer(self, logg):
		file_name = os.path.join(os.path.dirname(__file__), self.__file_name + ".log")
		
		with open(file_name, "a") as file:
			file.write(logg +"\n")
	
	def loggue(self,
	message,
	datefmt="%Y-%m-%d %H:%M:%S", sep=" ==> ",isfile=False):
		data = datetime.now().strftime(datefmt)
		self.file_logguer(f"{data}{sep}{message}")
		
		
	
	def debug(self,msg="(-_-)", logg=True, filename="debug"):
		self.loggue(message=f'cont: {self.cont} ---- time-tot: {self.sum:.3f} --- {msg} ----°--°---- {time.time() - self.init_time if logg else 0.000:.3f}')
		self.sum +=  time.time() -self.init_time
		self.init_time = time.time()
		self.cont  += 1
		




def log_com_tempo():
    tempo_inicial = time.time()
    logging.info(f"Inicio: 0.000")

    ultimo_tempo = tempo_inicial

    for i in range(5):  # Simula 5 logs
        time.sleep(2)  # Simula uma espera entre os logs (2 segundos)
        tempo_atual = time.time()
        diferenca = tempo_atual - ultimo_tempo
        logging.info(f"{diferenca:.3f}")
        ultimo_tempo = tempo_atual




if __name__ == "__main__":
    active = ActivationTime()
    active.clear()
    active.debug(logg=False)
    active.debug()
    time.sleep(2)
    active.debug()
    