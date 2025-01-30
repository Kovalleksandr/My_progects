from datetime import datetime, date, timedelta


# Функція для перетворення рядка у дату (об'єкт datetime.date)
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


# Функція для перетворення об'єкта datetime.date у рядок у форматі "YYYY.MM.DD"
def date_to_string(date):
    return date.strftime("%Y.%m.%d")


# Функція для підготовки списку користувачів (перетворення рядка дати у об'єкт datetime.date)
def prepare_user_list(user_data):
    return [{"name": user["name"], "birthday": string_to_date(user["birthday"])} for user in user_data]


# Функція для знаходження наступного вказаного дня тижня (0 = понеділок)
def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:  # Якщо день вже минув або це сьогодні, додаємо 7 днів
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


# Функція для перенесення дати на наступний робочий день, якщо вона припадає на вихідний
def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # 5 = субота, 6 = неділя
        return find_next_weekday(birthday, 0)  # Знаходимо наступний понеділок
    return birthday


# Функція для знаходження майбутніх днів народження
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()  # Поточна дата

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Перевіряємо, чи день народження вже минув у цьому році
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Обчислюємо кількість днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Якщо день народження настає у найближчі `days` днів, додаємо до списку
        if 0 <= days_until_birthday <= days:
            # Перенесення привітання на наступний робочий день, якщо день випадає на вихідний
            congratulation_date = adjust_for_weekend(birthday_this_year)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays


# Вхідні дані (список користувачів)
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# Використання функцій
prepared_users = prepare_user_list(users)  # Підготовка списку користувачів
upcoming_birthdays = get_upcoming_birthdays(prepared_users, 7)  # Пошук найближчих днів народження

# Вивід результату
print(upcoming_birthdays)
