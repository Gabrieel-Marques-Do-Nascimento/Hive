import jwt
from datetime import datetime, timedelta
import time


class TokenCreator:
    """
            As propriedades são armazenadas como privadas (prefixadas por __), ou seja, só podem ser acessadas dentro da classe.
    :Param:
        token_key (str): Chave secreta usada para assinar os tokens.
        exp_time_min: Tempo (em minutos) até o token expirar.
        refresh_time_min: Tempo
    em minutos) antes da expiração para que o token possa ser renovado (refresh).
    """

    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min

    def creat(self, uid: int) -> str:
        """
        Cria um token JWT com base no UID fornecido.
        :param uid: O UID do usuário para o qual o token será criado.
        :return: O token JWT.
        """
        return self.__enconde_token(uid=uid)

    def refesh(self, token: str) -> str:
        """O método refesh verifica se um token está próximo da expiração (com base em __REFRESH_TIME_MIN). Caso esteja, ele cria um novo token; caso contrário, retorna o token atual.

        Args:
            token (str): TOKEN do usuario

        Returns:
            str: TOKEN DO USUARIO
        """
        token_information = jwt.decode(
            token, key=self.__TOKEN_KEY, algorithms='HS256')
        token_uid = token_information["uid"]
        exp_time = token_information["exp"]

        if ((exp_time - time.time()) / 60) < self.__REFRESH_TIME_MIN:
            return self.__enconde_token(token_uid)
        return token

    def __enconde_token(self, uid: int) -> str:
        """O método __enconde_token é usado internamente para criar um novo token JWT com base no ID do usuário (uid) e na chave secreta (__TOKEN_KEY).
        """
        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN),
            "uid": uid  # id de ususario
        }, key=self.__TOKEN_KEY, algorithm='HS256')
        return token


class TokenUpdate:
    """
            As propriedades são armazenadas como privadas (prefixadas por __), ou seja, só podem ser acessadas dentro da classe.
    :Param:
        token_key (str): Chave secreta usada para assinar os tokens.
        exp_time_min: Tempo (em minutos) até o token expirar.
        refresh_time_min: Tempo
    em minutos) antes da expiração para que o token possa ser renovado (refresh).
    """

    def __init__(self, token_key: str, exp_time_day: int, refresh_time_day: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_DAY = exp_time_day
        self.__REFRESH_TIME_DAY = refresh_time_day

    def creat(self, uid: int) -> str:
        """
        Cria um token JWT com base no UID fornecido.
        :param uid: O UID do usuário para o qual o token será criado.
        :return: O token JWT.
        """
        return self.__enconde_token(uid=uid)

    def refesh(self, token: str) -> str | None:
        """O método refesh verifica se um token está próximo da expiração (com base em __REFRESH_TIME_MIN). Caso esteja, ele cria um novo token; caso contrário, retorna o token atual.

        Args:
            token (str): TOKEN do usuario

        Returns:
            str: TOKEN DO USUARIO
        """
        token_information = jwt.decode(
            token, key=self.__TOKEN_KEY, algorithms='HS256')
        token_uid = token_information["uid"]
        exp_time = token_information["exp"]
        if datetime.fromtimestamp(exp_time).year != datetime.now().year:
            return None
        if datetime.fromtimestamp(exp_time).month != datetime.now().month:
            return None
        if (datetime.fromtimestamp(exp_time).day - self.__REFRESH_TIME_DAY) > datetime.now().day:
            return self.__enconde_token(token_uid)
        return token

    def __enconde_token(self, uid: int) -> str:
        """O método __enconde_token é usado internamente para criar um novo token JWT com base no ID do usuário (uid) e na chave secreta (__TOKEN_KEY).
        """
        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(days=self.__EXP_TIME_DAY),
            "uid": uid  # id de ususario
        }, key=self.__TOKEN_KEY, algorithm='HS256')
        return token
    
if __name__ == '__main__':
    print('====================== teste token creater ======================')
    token_creator = TokenCreator(token_key='123456', exp_time_min=1, refresh_time_min=1)
    token = token_creator.creat(uid=1)
    print(token)
    print(token_creator.refesh(token=token))
    print('======================= Token update ========================')
    token_update = TokenUpdate(token_key='123456', exp_time_day=15, refresh_time_day=5)
    token = token_update.creat(uid=1)
    print(token)
    print(jwt.decode(
            token, key='123456', algorithms='HS256'))
    print(datetime.fromtimestamp(jwt.decode(
            token, key='123456', algorithms='HS256')['exp']))
