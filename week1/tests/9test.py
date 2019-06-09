from io import StringIO
from ..matrix_script9 import *

test1 = StringIO("7 3\nTsi\nh%x\ni #\nsM \n$a \n#t%\nir!\n")
test2 = StringIO("1 1\na\n")
test3 = StringIO("1 2\nad\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert matr() == "This is Matrix#  %!"


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert matr() == "a"


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert matr() == "ad"
