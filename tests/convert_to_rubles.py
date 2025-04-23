import os
import requests
from typing import Dict


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции, включая сумму и код валюты.
    :return: Сумма в рублях.
    """
    # Достаём данные из структуры транзакции
    amount = transaction.get("operationAmount", {}).get("amount", 0)
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    # Если валюта уже в рублях, возвращаем сумму
    if currency_code == "RUB":
        return float(amount)

    # Получаем API ключ из переменных окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не задан в переменных окружения")

    # Исправляем URL на корректный для API
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "from": currency_code,
        "to": "RUB",
        "amount": amount
    }
    headers = {"apikey": api_key}

    # Выполняем запрос к API
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Ошибка API: {response.status_code}")

    # Извлекаем конвертированную сумму из ответа API
    data = response.json()
    return round(data.get("result", 0), 2)
