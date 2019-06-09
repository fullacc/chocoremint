from io import StringIO
from ..validating_credit_card_number7 import *

test1 = StringIO(
    "6\n4123456789123456\n5123-4567-8912-3456\n61234-567-8912-3456\n4123356789123456\n5133-3367-8912-3456\n5123 - 3567 - 8912 - 3456\n"
)
test2 = StringIO("1\n8278929\n")
test3 = StringIO("1\n7727298200209\n")

def test_case_1(monkeypatch):
    monkeypatch.setattr("sys.stdin", test1)
    assert validate() == ["Valid", "Valid", "Invalid", "Valid", "Invalid", "Invalid"]


def test_case_2(monkeypatch):
    monkeypatch.setattr("sys.stdin", test2)
    assert validate() == ["Invalid"]


def test_case_3(monkeypatch):
    monkeypatch.setattr("sys.stdin", test3)
    assert validate() == ["Invalid"]
