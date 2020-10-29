import pytest
from programs.string_times import string_times

def test_string_times():
    assert string_times("Hi", 0) == ''
    assert string_times("Hello", 3) == "HelloHelloHello"