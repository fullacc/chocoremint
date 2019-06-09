from io import StringIO
from ..iterables_and_iterators8 import *

test1 = StringIO("4\na a c d\n2\n")
test2 = StringIO("2\na a\n2\n")
test3 = StringIO("4\na a a a\n2\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert iterables() == 0.8333333333333334


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert iterables() == 1.0


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert iterables() == 1.0
