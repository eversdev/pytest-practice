import pytest

def reverse_string(my_string):
    return my_string[::-1]


def test_reverse_string():
    assert reverse_string("hello") == "olleh"



