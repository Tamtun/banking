import re
from typing import List, Dict
from collections import Counter

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


def group_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Counter[str]:
    """
    Подсчитывает количество транзакций для каждой категории.
    Если категория встречается в описании транзакции (без учёта регистра), увеличивает счётчик.

    :param transactions: Список транзакций (словарей).
    :param categories: Список категорий для поиска.
    :return: Counter с количеством транзакций для каждой категории.
    """
    counter = Counter()
    for transaction in transactions:
        # Приводим описание транзакции к нижнему регистру для корректного поиска
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return counter
