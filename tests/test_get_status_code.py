from unittest.mock import patch
from app.get_status_code import get_status_code

@patch("app.get_status_code.requests.get")
def test_get_status_code(mock_get_status_code):
    mock_get_status_code.return_value.status_code = 200
    result = get_status_code("https://example.com")
    assert result == 200


