import pytest
from programs.front_back import front_back

def test_front_back():
    assert front_back("code") == "eodc"
    assert front_back("a") == "a"