import pytest



def test_even_or_odd():
    assert even_or_odd(2) == "even"


def even_or_odd(num):
    return "even" if num % 2 == 0 else "odd"


