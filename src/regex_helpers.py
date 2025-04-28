import re
from typing import List, Dict


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует транзакции, описание которых содержит указанную строку.

    :param transactions: Список транзакций.
    :param search_string: Строка поиска.
    :return: Список транзакций с совпадением в описании.
    """
    return [
        transaction
        for transaction in transactions
        if re.search(search_string, transaction.get("description", ""), re.IGNORECASE)
    ]


def group_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Группирует транзакции по категориям.

    :param transactions: Список транзакций.
    :param categories: Список категорий.
    :return: Словарь с количеством транзакций в каждой категории.
    """
    result = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "").lower()  # Приведение к нижнему регистру
        for category in categories:
            # Условие для поиска категории как подстроки в описании
            if category.lower() in description:
                result[category] += 1
    return result
