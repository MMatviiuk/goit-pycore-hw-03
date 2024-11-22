import re
from typing import List

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до міжнародного формату.

    Параметри:
    phone_number (str): Сировий рядок з номером телефону.

    Повертає:
    str: Нормалізований телефонний номер у міжнародному форматі або 'Invalid phone number'.
    """
    # Видаляємо всі символи, окрім цифр
    pattern = r"\D"
    replacement = ""
    phone_number = re.sub(pattern, replacement, phone_number)

    # Перевіряємо довжину номеру та додаємо необхідний код країни
    if len(phone_number) == 12 and phone_number.startswith("380"):
        # Якщо номер вже починається з коду України, просто додаємо '+'
        return f'+{phone_number}'
    elif len(phone_number) == 10:
        # Якщо номер має 10 цифр (без коду країни), додаємо '+38'
        return f'+38{phone_number}'
    else:
        return 'Invalid phone number'

# Приклади використання
raw_numbers: List[str] = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
    " 8(950)1234567",
    " 1234567",
    "123-456",
    "38050123ABCD",
    "\\380501234567"
]

sanitized_numbers: List[str] = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
