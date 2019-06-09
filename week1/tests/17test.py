import pytest
from io import StringIO
from ..word_order17 import *

test1 = StringIO("4\nbcdef\nabcdefg\nbcde\nbcdef\n")
test2 = StringIO("4\nbcdef\nabcdefg\nbcde\nbcdef\n")
test3 = StringIO("4\nbcdef\nabcdefg\nbcde\nbcdef\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert word_order() == [3,[2,1,1]]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert word_order() == [3,[2,1,1]]


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert word_order() == [3,[2,1,1]]
