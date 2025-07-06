import pytest

@pytest.fixture
def numbers():
    return [1,2,3]

def test_numbers(numbers):
    assert len(numbers) == 3

