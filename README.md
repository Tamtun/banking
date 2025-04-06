# Banking Masking Utility

Этот проект представляет собой набор утилит для работы с номерами банковских карт и счетов, а также для обработки и сортировки данных.

## Функции

### Маскировка номеров карт и счетов  
- **`get_mask_card_number(card_number: str) -> str`** — маскирует номер карты в формате `XXXX XX** **** XXXX`.  
- **`get_mask_account(account_number: str) -> str`** — маскирует номер счета в формате `**XXXX`.  
- **`mask_account_card(data: str) -> str`** — определяет тип данных и применяет соответствующую маскировку.  

### Фильтрация и сортировка данных  
- **`filter_by_state(data: list, state='EXECUTED') -> list`** — фильтрует список словарей по значению ключа `state`, возвращая только соответствующие записи.  
- **`sort_by_date(data: list, descending=True) -> list`** — сортирует список словарей по дате (`date`), по умолчанию в порядке убывания.  

### Генераторы данных
- **`filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]`** — возвращает только транзакции с заданной валютой.

- **`transaction_descriptions(transactions: list[dict]) -> Iterator[str]`** — возвращает описания транзакций.

- **`card_number_generator(start: int, end: int) -> Iterator[str]`** — генерирует номера карт в формате XXXX XXXX XXXX XXXX для заданного диапазона.

## Установка и использование

1. Клонируйте репозиторий:

   git clone <URL-вашего-репозитория>
   cd <название-проекта>
   
## Установка зависимостей  

1. Установите Python 3.10+  
2. Установите виртуальное окружение и активируйте его:

   python -m venv venv
   source venv/bin/activate  # для macOS и Linux
   venv\Scripts\activate  # для Windows
3. Установите зависимости:

   pip install -r requirements.txt 

## Тестирование
В проекте используются модульные тесты с `pytest`.  
Для запуска тестов выполните команду:
    pytest

Для проверки покрытия кода тестами используйте:
   pytest --cov=src
