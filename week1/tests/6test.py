from io import StringIO
from ..the_minion_game6 import *

test1 = StringIO('BANANA\n')
test2 = StringIO('44\n')

def test_case_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', test1)
    assert main() == ["Stuart",12]

def test_case_2(monkeypatch):
    monkeypatch.setattr('sys.stdin', test2)
    assert main() == True