from datetime import datetime
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Принимает список словарей и опционально значение для ключа.
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует значению.
    """
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки.
    Возвращает новый список, отсортированный по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)
