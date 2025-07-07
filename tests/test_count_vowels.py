import pytest

def test_count_vowels():
    assert count_vowels("My string") == 1



def count_vowels(my_str):
    return sum(1 for i in my_str if i in "aeiou")
