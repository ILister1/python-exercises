import pytest
from programs import factorial

def test_fact():
    assert factorial.fact(0) == 1