import pytest

def test_count_vowels():
    assert count_vowels("My string") == 1



def count_vowels(my_str):
    counter = 0
    for i in my_str:
        if i in "aeiou":
            counter+=1
    return counter
