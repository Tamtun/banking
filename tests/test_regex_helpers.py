from src.regex_helpers import filter_transactions_by_description, group_transactions_by_category


def test_filter_transactions_by_description():
    transactions = [
        {"description": "Оплата услуг связи"},
        {"description": "Покупка продуктов"},
        {"description": "Оплата проезда"},
    ]
    search_string = "оплата"
    result = filter_transactions_by_description(transactions, search_string)
    assert len(result) == 2
    assert result[0]["description"] == "Оплата услуг связи"
    assert result[1]["description"] == "Оплата проезда"


def test_group_transactions_by_category_simple():
    """Тест с максимально простыми и предсказуемыми данными"""
    transactions = [
        {"description": "услуги"},  # Только категория
        {"description": "продукты"},
        {"description": "проезд"},
    ]
    categories = ["услуги", "продукты", "проезд"]
    result = group_transactions_by_category(transactions, categories)

    assert result == {"услуги": 1, "продукты": 1, "проезд": 1}, f"Получен результат: {result}"
