# Кости
# Демонстрирует генерацию случайных чисел

import random

# Создаем случайные числа из диапазона 1 - 6
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# """Второй способ - можно использовать функцию randrange,
# но в ней отсчёт идёт с нуля, поэтому добавляем +1 и начало идёт с 1"""
# die1 = random.randrange(6) + 1
# die2 = random.randrange(6) + 1

total = die1 + die2

print("Пpи вашем броске выпало", die1, "и", die2, "очков. В сумме", total)

input("\n\nНажмите Enter, чтобы выйти.")
