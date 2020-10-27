import pytest
from programs import list_of_squares

def test_list():
    assert list_of_squares.list_of_squares(1) == {1: 1}

