import pytest
from io import StringIO
from ..piling_up13 import pilingup

test1 = StringIO("2\n6\n4 3 2 1 3 4\n3\n1 3 2\n")
test2 = StringIO("Chocofood1112\n")
test3 = StringIO("\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert pilingup() == ["Yes", "No"]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert pilingup() == "cdfhooooC1112"


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert pilingup() == ""
