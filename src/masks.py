import logging
import os
import json
from typing import List, Dict

# Настройка логгера для модуля utils
log_file = os.path.join("logs", "utils.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень DEBUG

file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.DEBUG)  # Уровень для файла
formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает список финансовых транзакций из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список транзакций или пустой список, если файл недоступен, пустой или некорректен.
    """
    try:
        logger.info("Попытка загрузки файла: %s", file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл успешно загружен. Количество транзакций: %d", len(data))
                return data
            else:
                logger.warning("Файл не содержит списка транзакций: %s", file_path)
                return []
    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
        return []
    except json.JSONDecodeError as e:
        logger.error("Ошибка декодирования JSON-файла: %s. Ошибка: %s", file_path, str(e))
        return []