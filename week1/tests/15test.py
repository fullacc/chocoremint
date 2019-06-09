import pytest
from io import StringIO
from ..print_function15 import *

test1 = StringIO("3\n")
test2 = StringIO("4\n")
test3 = StringIO("5\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert printf() == '123'


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert printf() == '1234'


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert printf() == '12345'
