import pytest


@pytest.fixture
def sample_card_numbers() -> list[tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]


@pytest.fixture
def sample_account_numbers() -> list[tuple[str, str]]:
    return [
        ("40817810099910004312", "**4312"),
        ("1234567890123456", "**3456"),
    ]


@pytest.fixture
def sample_sort_data() -> list[dict[str, str | int]]:
    return [
        {"id": 1, "date": "2024-03-01"},
        {"id": 2, "date": "2024-01-15"},
        {"id": 3, "date": "2024-02-10"},
    ]
