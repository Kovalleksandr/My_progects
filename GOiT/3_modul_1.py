from datetime import datetime


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    # Конвертуємо об'єкт datetime у рядок
    return date.strftime("%Y.%m.%d")

date_string = "2024.01.01"  
converted_date = string_to_date(date_string)
print(converted_date)  

date_string_back = date_to_string(converted_date) 
print(date_string_back) 
