from unittest.mock import patch
from tests import wait_and_return as w



@patch("tests.wait_and_return.time.sleep")
def test_wait_and_return(mock_sleep):
    mock_sleep.return_value = None
    result = w.wait_and_return("hi")
    assert result == "hi"

