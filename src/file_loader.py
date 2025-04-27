import logging
import pandas as pd
from typing import List, Dict

# Настройка логгера для модуля file_loader
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/file_loader.log", mode="w")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь до CSV-файла.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        logger.info("Попытка загрузки CSV-файла: %s", file_path)
        data = pd.read_csv(file_path)
        transactions = data.to_dict(orient="records")
        logger.info("CSV-файл успешно загружен. Количество транзакций: %d", len(transactions))
        return transactions
    except FileNotFoundError:
        logger.error("CSV-файл не найден: %s", file_path)
        return []
    except pd.errors.EmptyDataError:
        logger.error("CSV-файл пуст: %s", file_path)
        return []


def load_transactions_from_xlsx(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из XLSX-файла.

    :param file_path: Путь до XLSX-файла.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        logger.info("Попытка загрузки XLSX-файла: %s", file_path)
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        logger.info("XLSX-файл успешно загружен. Количество транзакций: %d", len(transactions))
        return transactions
    except FileNotFoundError:
        logger.error("XLSX-файл не найден: %s", file_path)
        return []
    except pd.errors.EmptyDataError:
        logger.error("XLSX-файл пуст: %s", file_path)
        return []
