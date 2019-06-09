from io import StringIO
from ..iterables_and_iterators8 import *

test1 = StringIO("4\na a c d\n2")
test2 = StringIO("44\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert iterables() == 0.8333333333333334


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert main() == True
