from datetime import datetime

# Функція для перетворення рядка у дату
def string_to_date(date_string):
    # Конвертуємо рядок у об'єкт datetime
    return datetime.strptime(date_string, "%Y.%m.%d")

# Функція для перетворення дати у рядок
def date_to_string(date):
    # Конвертуємо об'єкт datetime у рядок
    return date.strftime("%Y.%m.%d")

# Використання функцій
date_string = "2024.01.01"  # Вхідний рядок дати
converted_date = string_to_date(date_string)  # Перетворення у дату
print(converted_date.date())
print(converted_date)
date_string_back = date_to_string(converted_date)  # Перетворення назад у рядок
print("Converted back to string:", date_string_back)  # Вивід рядка
