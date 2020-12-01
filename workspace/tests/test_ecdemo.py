from ecdemo import __version__
from ecdemo.user import Fullname


def test_version():
    assert __version__ == '0.1.0'


def test_name_length():
    assert Fullname('Tanaka', 'Taro')


def test_name_max_length():
    assert Fullname('12345678901234567890', 'Taro')


def test_name_min_length():
    assert Fullname('N', 'A')
