import pytest

def test_find_max():
    assert find_max([1,2,3]) == 3


def find_max(my_list):
    return max(my_list)
