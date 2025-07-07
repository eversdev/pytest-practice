import pytest

def test_is_palindrome():
    assert is_palindrome("racecar") is True

def is_palindrome(my_str):
    if my_str == my_str[::-1]:
        return True
    else:
        return False


