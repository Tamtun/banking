import pytest
from src.widget import mask_account_card, get_date

""" Тесты """


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Счет 40817810099910004312", "Счет **4312"),
        ("VISA 1234567812345678", "VISA 1234 56** **** 5678"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-01", "01.03.2024"),
        ("2000-01-01", "01.01.2000"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected
