import pytest

def add_and_multiply(x, y):
    return (x + y) * (x - y)

def test_add_and_multiply():
    assert add_and_multiply(2,3) == -5


