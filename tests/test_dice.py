from unittest.mock import patch
from tests import dice as d

@patch("tests.dice.roll_dice")
def test_dice(mock_roll_dice):
    mock_roll_dice.return_value = 4
    result = d.roll_dice()
    assert result == 4




