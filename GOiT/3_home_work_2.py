import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if not (1 <= min <= 1000) or not (1 <= max <= 1000) or not (min <= quantity <= max):
        return []
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))

'''
Навіщо перевірка (min <= quantity <= max)???
--------------------------------------------
Ця перевірка гарантує, що quantity (кількість чисел, які треба вибрати) знаходиться в межах [min, max].
Наприклад, якщо користувач введе get_numbers_ticket(1, 10, 15),
то це некоректний запит, адже в діапазоні від 1 до 10 всього 10 чисел, а вибрати потрібно 15.
Перевірка min <= quantity <= max поверне False, і функція поверне [].


Навіщо max + 1???
-----------------
вказаний діапазон, наприклад 1, 50, буде виводити числа від 1 до 49, тому використовуєма значення + 1
'''



