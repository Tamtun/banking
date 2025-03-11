# Banking Masking Utility

Этот проект представляет собой набор утилит для работы с номерами банковских карт и счетов.  

## Функции

- **Маскировка номеров карт и счетов**  
  - `get_mask_card_number(card_number: str) -> str` — маскирует номер карты в формате `XXXX XX** **** XXXX`.  
  - `get_mask_account(account_number: str) -> str` — маскирует номер счета в формате `**XXXX`.  
  - `mask_account_card(data: str) -> str` — определяет тип данных и применяет соответствующую маскировку.  