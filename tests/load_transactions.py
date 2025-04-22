import pytest
from src.utils import load_transactions
import json
from unittest.mock import mock_open, patch


def test_load_transactions_valid():
    mock_data = '[{"amount": 100, "currency": "USD"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        transactions = load_transactions("data/operations.json")
        assert transactions == [{"amount": 100, "currency": "USD"}]


def test_load_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data="{invalid_json}")):
        transactions = load_transactions("data/operations.json")
        assert transactions == []


def test_load_transactions_file_not_found():
    transactions = load_transactions("data/nonexistent.json")
    assert transactions == []
