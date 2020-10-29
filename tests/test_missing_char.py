import pytest
from programs.missing_char import missing_char

def test_missing():
    assert missing_char('kitten', 0) == 'itten'