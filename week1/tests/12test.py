import pytest
from io import StringIO
from ..ginorts12 import ginorts

test1 = StringIO("Sorting1234\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert ginorts() == "ginortS1324"


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
