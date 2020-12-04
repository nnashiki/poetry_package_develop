from typing import Protocol

NAME_MAX_LENGTH = 20
NAME_MIN_LENGTH = 1


class Fullname:
    def __init__(self,
                 family: str,
                 first: str):
        self.family = self.common_name_validate(family)
        self.first = self.common_name_validate(first)

    @staticmethod
    def common_name_validate(name):
        if len(name) > NAME_MAX_LENGTH:
            raise NameLengthException
        elif len(name) < NAME_MIN_LENGTH:
            raise NameLengthException
        return name


class NameLengthException(Exception):
    pass


class User:
    def __init__(self,
                 name: Fullname):
        self.name: Fullname = name

    @classmethod
    def init_user(cls, name: Fullname):
        return cls(name)


class InterfaceUserRepository(Protocol):
    def find(self, name: Fullname) -> User:
        pass

    def save(self, user: User) -> None:
        pass

    def exists(self, name: Fullname) -> bool:
        pass


class UserRepositoryPostgres:
    pass


class UserRepositoryMock:

    @staticmethod
    def find(name: Fullname) -> User:
        return User(Fullname('Tanaka', 'Taro'))

    @staticmethod
    def save(user: User) -> None:
        pass

    @staticmethod
    def exists(name: Fullname) -> bool:
        return False


def save_process(repository: InterfaceUserRepository,
                 user: User):
    if repository.exists(user.name):
        return Exception('登録済みです')

    repository.save(user)
    find_result: User = repository.find(user.name)
    print(find_result.name)
