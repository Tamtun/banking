from typing import List, Dict, Union
import pytest
from src.processing import filter_by_state, sort_by_date

""" Тесты """


@pytest.mark.parametrize(
    "state, expected",
    [
        ("done", [{"id": 1, "state": "done"}, {"id": 3, "state": "done"}]),
        ("pending", [{"id": 2, "state": "pending"}]),
        ("canceled", []),
    ],
)
def test_filter_by_state(state: str, expected: List[Dict[str, Union[str, int]]]) -> None:
    data: List[Dict[str, Union[str, int]]] = [
        {"id": 1, "state": "done"},
        {"id": 2, "state": "pending"},
        {"id": 3, "state": "done"},
    ]
    assert filter_by_state(data, state) == expected


def test_sort_by_date(sample_sort_data) -> None:
    assert sort_by_date(sample_sort_data) == [
        {"id": 1, "date": "2024-03-01"},
        {"id": 3, "date": "2024-02-10"},
        {"id": 2, "date": "2024-01-15"},
    ]
