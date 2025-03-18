from Database import Users, db


class Get_User:
    """
    Classe para obter informações de usuário.
    """
    def __init__(self) -> None:
        pass

    def id(self, id: int) -> Users:
        """
        Retorna o usuário com o id fornecido.
        """
        return Users.query.filter_by(id=id).first()
