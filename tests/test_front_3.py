import pytest
from programs.front_3 import front_3

def test_front_3():
    assert front_3("to") == "to"
    assert front_3("chocolate") == "chochocho"