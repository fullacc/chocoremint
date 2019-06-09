import pytest
from io import StringIO
from ..ginorts12 import ginorts

test1 = StringIO("Sorting1234\n")
test2 = StringIO("Chocofood1112\n")
test3 = StringIO("\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert ginorts() == "ginortS1324"


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert ginorts() == "cdfhooooC1112"


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert ginorts() == ""
