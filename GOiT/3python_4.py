from datetime import datetime, date


# Функція для перетворення рядка у дату (об'єкт datetime.date)
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


# Функція для перетворення об'єкта datetime.date у рядок у форматі "YYYY.MM.DD"
def date_to_string(date):
    return date.strftime("%Y.%m.%d")


# Функція для підготовки списку користувачів (перетворення рядка дати у об'єкт datetime.date)
def prepare_user_list(user_data):
    return [{"name": user["name"], "birthday": string_to_date(user["birthday"])} for user in user_data]


# Функція для знаходження майбутніх днів народження
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()  # Поточна дата

    for user in users:
        # Отримуємо дату дня народження у поточному році
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо день народження вже минув у поточному році, беремо його у наступному році
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Обчислюємо кількість днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Якщо день народження настає у найближчі `days` днів, додаємо до списку
        if 0 <= days_until_birthday <= days:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(birthday_this_year)
            })

    return upcoming_birthdays  # Повертаємо список майбутніх днів народження


# Вхідні дані (список користувачів)
users = [
    {"name": "Sarah Lee", "birthday": "1957.03.30"},
    {"name": "John Doe", "birthday": "1985.01.30"},
    {"name": "Jane Smith", "birthday": "1990.03.27"},
    {"name": "Mike Johnson", "birthday": "1985.01.23"},  # Дубльованого "John Doe" виправлено
]

# Використання функцій
prepared_users = prepare_user_list(users)  # Підготовка списку користувачів
upcoming_birthdays = get_upcoming_birthdays(prepared_users, 7)  # Пошук найближчих днів народження

# Вивід результату
print(upcoming_birthdays)
