import pytest
from io import StringIO
from ..time_delta16 import *

test1 = StringIO("1\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\n")
test2 = StringIO("1\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000\n")
test3 = StringIO("1\nSun 10 May 2015 13:54:36 -0700\nFri 01 May 2015 13:54:36 -0000\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert timedelta() == [25200]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert timedelta() == [88200]


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert timedelta() == [802800]
