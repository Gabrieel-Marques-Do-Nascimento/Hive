import logging
import time
import os
from datetime import datetime


import time
import os
from datetime import datetime


class ActivationTime:
    def __init__(self, is__file__):
        self.init_time = time.time()
        self.cont = 1
        self.__file_name = "logguer"
        self.__file__ = os.path.dirname(
            is__file__) if is__file__ else os.getcwd()
        self.dirname = os.path.join(self.__file__, "logs")
        self.sum = 0

        # Criar diretório logs se não existir
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)

    def file_name(self, name, path=None, filetimename=False):
        if path:
            self.dirname = os.path.join(self.__file__, path)

        if filetimename:
            name += datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        self.__file_name = os.path.join(self.dirname, name)

    def clear(self):
        file_path = self.__file_name + ".log"
        with open(file_path, "w") as file:
            file.write("")

    def file_logguer(self, logg):
        file_path = self.__file_name + ".log"
        with open(file_path, "a") as file:
            file.write(logg + "\n")

    def loggue(self, message, datefmt="%Y-%m-%d %H:%M:%S", sep=" ==> "):
        data = datetime.now().strftime(datefmt)
        self.file_logguer(f"{data}{sep}{message}")

    def debug(self, msg="(-_-)", logg=True):
        tempo_decorrido = time.time() - self.init_time if logg else 0.000
        self.sum += tempo_decorrido

        message = (
            f"[LOG {self.cont}] "
            f"Tempo desde o último log: {tempo_decorrido:.3f}s | "
            f"Tempo total: {self.sum:.3f}s | "
            f"Mensagem: {msg}"
        )

        self.loggue(message)

        self.init_time = time.time()
        self.cont += 1


def time_init(file):

    def decorator(function):
        a = ActivationTime(file)
        a.file_name("decorator")

        def wharaper(*args, **kwargs):
            init = time.time()
            result = function(*args, **kwargs)
            tot = (time.time() - init) * 1000  # Converte para milissegundos
            a.loggue(message=f"tempo de execução: {tot:.3f}ms")
            return result
        return wharaper
    return decorator


def time_initF(file):
    def decorator(function):
        a = ActivationTime(file)

        def wrapper(*args, **kwargs):
            init = time.time()
            result = function(*args, **kwargs)
            tot = (time.time() - init) * 1000  # Converte para milissegundos
            a.loggue(f"Tempo de execução: {tot:.3f} ms")
            return result

        return wrapper
    return decorator


# ===========================================
# =====°===°=====     testes     =======°=°======
# ===========================================


if __name__ == "__main__":
    active = ActivationTime(is__file__=__file__)
    active.clear()
    active.debug(logg=False)
    active.debug()
    time.sleep(2)
    active.debug()

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

    @time_init("log.txt")
    def minha_funcao():
        time.sleep(1)
        print("Função executada")

    minha_funcao()
