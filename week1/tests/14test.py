import pytest
from io import StringIO
from ..company_logo14 import *

test1 = StringIO("aabbbccde\n")
test2 = StringIO("askldlksad\n")
test3 = StringIO("aaaaaaa\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert company_logo() == [["b", 3],["a", 2],["c", 2]]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert company_logo() == [['a',2],['d',2],['k',2]]


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert company_logo() == [['a',7]]
