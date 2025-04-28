import sys
from utils import load_transactions
from file_loader import load_transactions_from_csv, load_transactions_from_xlsx
from regex_helpers import filter_transactions_by_description, group_transactions_by_category
from masks import get_mask_account, get_mask_card_number
from external_api import convert_to_rubles
from processing import filter_by_state, sort_by_date
from decorators import log  # Если используете декораторы для логирования


# Оформляем логирование вызова main, если хотите отслеживать работу программы:
@log("logs/main.log")
def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()
    transactions = []

    if choice == "1":
        file_path = "data/operations.json"
        transactions = load_transactions(file_path)
        print("Для обработки выбран JSON‑файл.")
    elif choice == "2":
        file_path = "data/transactions.csv"
        transactions = load_transactions_from_csv(file_path)
        print("Для обработки выбран CSV‑файл.")
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        transactions = load_transactions_from_xlsx(file_path)
        print("Для обработки выбран XLSX‑файл.")
    else:
        print("Некорректный выбор. Программа завершена.")
        sys.exit(1)

    if not transactions:
        print("Не удалось загрузить транзакции. Завершаем работу.")
        sys.exit(1)

    # Фильтрация по статусу
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = (
            input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED/CANCELED/PENDING): ")
            .strip()
            .upper()
        )
        if status in statuses:
            # Если в данных ключ называется "status", используйте этот inline‑фильтр или переключитесь на filter_by_state,
            # если данные имеют ключ "state". Проверьте соответствие ключей!
            transactions = [t for t in transactions if t.get("status", "").upper() == status]
            print(f'Операции отфильтрованы по статусу "{status}".')
            break
        else:
            print(f'Статус "{status}" недоступен. Повторите ввод.')

    # Сортировка по дате с использованием processing.sort_by_date
    sort_choice = input("Отсортировать операции по дате? (да/нет): ").strip().lower()
    if sort_choice == "да":
        order = input("Введите порядок сортировки (asc для возрастания / desc для убывания): ").strip().lower()
        descending = order == "desc"
        transactions = sort_by_date(transactions, descending=descending)

    # Фильтрация или конвертация транзакций в рубли
    rubles_choice = input("Выводить только транзакции в рублях? (да/нет): ").strip().lower()
    if rubles_choice == "да":
        converted_transactions = []
        for t in transactions:
            if t.get("currency", "").upper() != "RUB":
                try:
                    # Конвертируем сумму в рубли и обновляем данные транзакции
                    t["amount"] = convert_to_rubles(t)
                    t["currency"] = "RUB"
                    converted_transactions.append(t)
                except Exception as e:
                    print(f"Не удалось конвертировать транзакцию: {e}")
            else:
                converted_transactions.append(t)
        transactions = converted_transactions

    # Фильтрация по ключевому слову в описании с использованием regex_helpers
    filter_choice = (
        input("Отфильтровать список транзакций по определенному слову в описании? (да/нет): ").strip().lower()
    )
    if filter_choice == "да":
        search_string = input("Введите слово для поиска: ").strip()
        transactions = filter_transactions_by_description(transactions, search_string)

    # Вывод итогового списка транзакций с применением маскировки номеров, если есть соответствующие ключи
    if transactions:
        print("\nРаспечатываю итоговый список транзакций...\n")
        for t in transactions:
            date = t.get("date", "Неизвестная дата")
            description = t.get("description", "Нет описания")
            # Маскировка номеров карт и счетов, если они присутствуют
            if "card_number" in t:
                try:
                    description += f" (Карточка: {get_mask_card_number(t['card_number'])})"
                except Exception:
                    description += " (Некорректный номер карты)"
            if "account_number" in t:
                try:
                    description += f" (Счет: {get_mask_account(t['account_number'])})"
                except Exception:
                    description += " (Некорректный номер счета)"

            print(f"{date} | {description}")
            print(f"Сумма: {t.get('amount', 0)} {t.get('currency', 'Неизвестная валюта')}")
            print("-" * 40)
        print(f"Всего транзакций: {len(transactions)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
