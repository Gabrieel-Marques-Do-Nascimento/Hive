class Base:
    def __init__(self, item):
        import re
        self.__re = re
        self.value = item


class Email(Base):
    def __init__(self, string: str):
        super().__init__(string)

    def is_valid(self):
        pattern = r'^[\w\.]+@[a-zA-z\d\.]+\.(com|site|ru|net|org)$'
        return self.__re.match(pattern, self.value)


class UserName(Base):
    def __init__(self, string: str):
        super().__init__(string)

class Password(Base):
    def __init__(self, string: str):
        super().__init__(string)