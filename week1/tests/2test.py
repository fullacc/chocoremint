import pytest

from week1.__main__ import *


def test_case_1():
    assert ifelse(3) == "Weird"
    assert ifelse(24) == "Not Weird"
    assert ifelse(9) == "Weird"