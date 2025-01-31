import re

def normalize_phone(phone_number):
    # Видаляємо всі зайві символи, залишаючи тільки цифри та '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # Якщо "+380", залишаємо без змін
    if cleaned_number.startswith("+380"):
        return cleaned_number

    # Якщо "380", додаємо "+"
    if cleaned_number.startswith("380"):
        return f"+{cleaned_number}"

    # Якщо починається з "0", додаємо "+38"
    if cleaned_number.startswith("0"):
        return f"+38{cleaned_number[1:]}"

    # Якщо номер містить тільки 9 або 10 цифр, додаємо "+38"
    if len(cleaned_number) in [9, 10]:
        return f"+38{cleaned_number}"

    
    return cleaned_number

# Приклад
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 12   ",
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
