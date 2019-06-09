import pytest
from io import StringIO
from ..merge_the_tools18 import *

test1 = StringIO("\n")
test2 = StringIO("\n")
test3 = StringIO("\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert () ==


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert () ==


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert () ==
