from typing import List, Dict


def filter_by_state(data: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Принимает список словарей и опционально значение для ключа.
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует значению.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
