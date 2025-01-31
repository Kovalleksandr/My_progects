from datetime import datetime

def get_days_from_today(date):
    try:
        date_today = datetime.today().date()                    # визначає сьогоднішю дату;(.date() - залишає дату, без часу)
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        difference_date = (date_today - date_object).days       # .days - залишає кількість днів, без часу
        return difference_date
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'YYYY-MM-DD'."

print(get_days_from_today("2024-02-13"))