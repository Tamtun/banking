from typing import Iterator, List, Dict


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Генератор, возвращающий транзакции с заданной валютой.
    """
    for tx in transactions:
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания произведенных транзакций.
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров карт в формат XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
