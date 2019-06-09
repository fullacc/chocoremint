from io import StringIO
from ..the_minion_game6 import *

test1 = StringIO("BANANA\n")
test2 = StringIO("STUART\n")
test3 = StringIO("KEVIN\n")


def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert minion_game() == ("Stuart", 12)


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert minion_game() == ("Stuart", 14)


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert minion_game() == ("Stuart", 9)
