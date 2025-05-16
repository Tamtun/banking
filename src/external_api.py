import os
import requests
from typing import Dict


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции.
    :return: Сумма в рублях.
    """
    base_currency = transaction.get("currency", "RUB")
    amount = transaction.get("amount", 0)

    if base_currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не задан в переменных окружения")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Ошибка API: {response.status_code}")

    rates = response.json().get("rates", {})
    rub_rate = rates.get("RUB")

    if not rub_rate:
        raise ValueError(f"Курс RUB для {base_currency} не найден")

    return round(float(amount) * rub_rate, 2)
