from ecdemo import __version__
from ecdemo.user import Fullname, NameLengthException, User, UserRepositoryMock, save_process

import pytest


def test_version():
    assert __version__ == '0.1.0'


class TestNameLength:

    def test_name_length(self):
        assert Fullname('Tanaka', 'Taro')

    def test_name_max_length(self):
        assert Fullname('12345678901234567890', 'Taro')

    def test_name_min_length(self):
        assert Fullname('N', 'A')

    def test_blank(self):
        with pytest.raises(NameLengthException):
            raise NameLengthException()


def test_user():
    user = User(Fullname('Tanaka', 'Taro'))
    dir(user)


def test_mock_repository():
    save_process(UserRepositoryMock, User(Fullname('Suzuki', 'Taro')))
