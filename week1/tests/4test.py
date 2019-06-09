from io import StringIO
from ..division4 import *

test1 = StringIO('4\n3\n')
test2 = StringIO('4\n5\n')

def test_case_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', test1)
    assert main() == (1,1.3333333333333333)

def test_case_2(monkeypatch):
    monkeypatch.setattr('sys.stdin', test2)
    assert main() == (0,0.8)