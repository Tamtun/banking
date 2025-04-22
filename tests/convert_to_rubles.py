import pytest
from unittest.mock import patch
from src.external_api import convert_to_rubles


@patch("os.getenv", return_value="mock_api_key")
@patch("requests.get")
def test_convert_to_rubles(mock_get, mock_env):
    mock_response = {"rates": {"RUB": 75.0}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rubles(transaction)
    assert result == 7500.0
