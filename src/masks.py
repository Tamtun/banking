import logging
import os

# Настройка логгера для модуля masks
log_file = os.path.join("logs", "masks.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="w"),
        logging.StreamHandler(),  # Опционально: для вывода логов в консоль
    ],
)
logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формат XXXX XX** **** XXXX."""
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error("Некорректный номер карты: %s", card_number)
            raise ValueError("Некорректный номер карты")

        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info("Успешно маскирован номер карты: %s -> %s", card_number, masked_card)
        return masked_card
    except Exception as e:
        logger.exception("Ошибка при маскировке номера карты: %s", str(e))
        raise


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формат **XXXX."""
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            logger.error("Некорректный номер счета: %s", account_number)
            raise ValueError("Некорректный номер счета")

        masked_account = f"**{account_number[-4:]}"
        logger.info("Успешно маскирован номер счета: %s -> %s", account_number, masked_account)
        return masked_account
    except Exception as e:
        logger.exception("Ошибка при маскировке номера счета: %s", str(e))
        raise
