import pytest
from programs import not_string

def test_not_string_with_not():
    assert not_string.not_string("not fair") == "not fair"
    assert not_string.not_string("with") == "not with"
    assert not_string.not_string("no") == "not no"

    