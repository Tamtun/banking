from typing import List
import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

""" Тесты """


def test_filter_by_currency_usd(sample_transactions: List[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 3
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in result)


def test_filter_by_currency_rub(sample_transactions: List[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "RUB" for tx in result)


def test_filter_by_currency_not_found(sample_transactions: List[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_content(sample_transactions: List[dict]) -> None:
    result = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected_descriptions


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, end, expected_count",
    [
        (1000, 1005, 6),  # включает 1000–1005 => 6 штук
        (1, 4, 4),  # включает 1–4 => 4
        (0, 0, 1),  # только 0
    ],
)
def test_card_number_generator_range(start: int, end: int, expected_count: int) -> None:
    cards = list(card_number_generator(start, end))
    assert len(cards) == expected_count
    for card in cards:
        assert isinstance(card, str)
        assert len(card) == 19
        assert all(part.isdigit() and len(part) == 4 for part in card.split())


def test_card_number_generator_format() -> None:
    cards = list(card_number_generator(10, 13))
    assert cards == ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012", "0000 0000 0000 0013"]
