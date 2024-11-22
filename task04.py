from datetime import datetime, timedelta, date
from typing import List, Dict

def is_date_within_days(target_date: datetime, days: int) -> bool:
    """
    Перевіряє, чи задана дата (ігноруючи рік) входить у наступні 'days' днів, включаючи сьогодні.
    Якщо дата вже пройшла цього року, розглядається дата наступного року.

    Параметри:
    target_date (datetime): Дата, яку потрібно перевірити.
    days (int): Кількість днів для перевірки.

    Повертає:
    bool: True, якщо дата входить у заданий діапазон, False інакше.
    """
    today_date = datetime.now().date()
    
    # Дата на поточний рік
    date_this_year = date(today_date.year, target_date.month, target_date.day)
    
    # Якщо дата вже пройшла, переносимо на наступний рік
    if date_this_year < today_date:
        target_date = date(today_date.year + 1, target_date.month, target_date.day)
    else:
        target_date = date_this_year
    
    # Перевіряємо, чи входить дата у діапазон наступних 'days' днів
    return today_date <= target_date <= (today_date + timedelta(days=days))

def adjust_to_weekday(date_obj: date) -> date:
    """
    Коригує задану дату на найближчий робочий день, якщо вона припадає на вихідні.

    Параметри:
    date_obj (date): Дата для коригування.

    Повертає:
    date: Скоригована дата.
    """
    # Якщо дата припадає на суботу, переносимо на понеділок
    if date_obj.weekday() == 5:  # Субота
        return date_obj + timedelta(days=2)
    # Якщо дата припадає на неділю, переносимо на понеділок
    elif date_obj.weekday() == 6:  # Неділя
        return date_obj + timedelta(days=1)
    return date_obj

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Створює список користувачів, чиї дні народження припадають на наступний тиждень.

    Параметри:
    users (List[Dict[str, str]]): Список словників з інформацією про користувачів (ключі 'name' та 'birthday').

    Повертає:
    List[Dict[str, str]]: Список словників з іменами користувачів та датами привітання.
    """
    upcoming_birthdays_list = []
    days = 7

    for user in users:
        try:
            # Конвертуємо дату народження з рядка у datetime об'єкт
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")

            # Перевіряємо, чи входить дата народження у наступний тиждень
            if is_date_within_days(user_birthday, days):

                current_year = datetime.now().year
                congratulation_date = date(current_year, user_birthday.month, user_birthday.day)
                
                # Коригуємо дату привітання, якщо вона припадає на вихідний
                congratulation_date = adjust_to_weekday(congratulation_date)

                # Додаємо користувача у список привітань
                upcoming_birthdays_list.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            # Пропускаємо користувачів з некоректним форматом дати
            pass

    return upcoming_birthdays_list

# Приклади використання
users = [
    {"name": "Jane", "birthday": "1990.07.05"},
    {"name": "Ted", "birthday": "1985.07.10"},
    {"name": "Mary", "birthday": "1990.07.13"},
    {"name": "Alice", "birthday": "1995.07.15"},
    {"name": "Bob", "birthday": "1995.07.07"},
    {"name": "Bob", "birthday": "1995.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
