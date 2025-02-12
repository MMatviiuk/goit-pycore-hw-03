import random
from typing import List

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Генерує відсортований список унікальних випадкових чисел для квитка.

    Параметри:
    min (int): Мінімальне можливе значення випадкового числа (має бути не менше 1).
    max (int): Максимальне можливе значення випадкового числа (має бути не більше 1000).
    quantity (int): Кількість унікальних випадкових чисел для генерації (має бути між min та max).

    Повертає:
    List[int]: Відсортований список унікальних випадкових чисел або порожній список, якщо параметри некоректні.
    """
    
    # Перевірка валідності вхідних параметрів
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        return []

    # Використання random.sample для отримання унікальних чисел
    return sorted(random.sample(range(min, max + 1), quantity))

# Приклади використання
print(get_numbers_ticket(1, 50, 5))    # Генерує 5 чисел від 1 до 50
print(get_numbers_ticket(-1, 50, 5))   # Невалідний мінімум, поверне []
print(get_numbers_ticket(1, 1001, 5))  # Невалідний максимум, поверне []
print(get_numbers_ticket(1, 5, 6))     # Більше чисел, ніж можливий діапазон, поверне []
