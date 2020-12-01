NAME_MAX_LENGTH = 20
NAME_MIN_LENGTH = 1


class NameLengthException(Exception):
    pass


class Fullname:
    def __init__(self,
                 family_name: str,
                 first_name: str):
        self.family_name = self.common_name_validate(family_name)
        self.first_name = self.common_name_validate(first_name)

    @staticmethod
    def common_name_validate(name):
        if len(name) > NAME_MAX_LENGTH:
            raise NameLengthException
        elif len(name) < NAME_MIN_LENGTH:
            raise NameLengthException
        return name


class User:
    def __init__(self,
                 name: str):
        self.name: str = name

    @classmethod
    def init_user(cls, name):
        return cls(name)
