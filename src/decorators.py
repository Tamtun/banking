import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызовов функции, результатов и ошибок.

    :param filename: Имя файла для записи логов. Если None, лог выводится в консоль.
    :return: Декорированная функция.
    """
    # Настраиваем логгер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter('%(message)s')

    if filename:
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                logger.info(f"Start function: {func_name}, Inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func_name} ok, Result: {result}")
                return result
            except Exception as e:
                logger.error(f"{func_name} error: {type(e).__name__}, Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
