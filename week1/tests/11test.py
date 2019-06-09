import pytest
from io import StringIO
from ..no_idea11 import noidea

test1 = StringIO('3 2\n1 5 3\n3 1\n5 7\n')



def test_case_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', test1)
    assert noidea() == 1
