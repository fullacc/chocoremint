from io import StringIO
from ..loops5 import *

test1 = StringIO("5\n")
test2 = StringIO("7\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert main() == [0, 1, 4, 9, 16]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert main() == [0, 1, 4, 9, 16, 25, 36]
