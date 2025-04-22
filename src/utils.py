import json
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает список финансовых транзакций из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список транзакций или пустой список, если файл недоступен, пустой или некорректен.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
