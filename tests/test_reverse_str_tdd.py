import pytest


def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def reverse_string(my_str):
    return my_str[::-1]
