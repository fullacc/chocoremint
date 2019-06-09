from io import StringIO
from ..write_a_function33 import *

test1 = StringIO("1897\n")
test2 = StringIO("44\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert main() == False


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert main() == True
