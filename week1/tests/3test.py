from io import StringIO
from ..arithmetic_operators3 import *

test1 = StringIO("3\n2\n")
test2 = StringIO("4\n5\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert count() == (5, 1, 6)


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert count() == (9, -1, 20)
