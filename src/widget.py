from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в переданной строке."""
    parts = data.rsplit(" ", 1)
    if len(parts) != 2 or not parts[1].isdigit():
        raise ValueError("Некорректный формат данных")

    name, number = parts
    masked_number = get_mask_account(number) if name.startswith("Счет") else get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Формат даты в 'ДД.ММ.ГГГГ'."""
    try:
        return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")
