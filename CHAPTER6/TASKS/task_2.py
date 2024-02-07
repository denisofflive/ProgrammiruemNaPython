# Доработайте игру «Отгадай число» из главы З так,
# чтобы в ней нашла применение функция ask_number().

# Игра "отгадай число"

import random

print("\t\tДобро пожаловать в игру 'Отгадай число'!")
print("Компьютер загадал натуральное число из диапазона от 1 до 100.")
print("Попытайтесь отгадать его зха минимальное число попыток.\n")

# Вводим функцию
def ask_number(question, low, high,):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

# Начальные значения
the_number = random.randint(1, 100)
guess = int(ask_number("Ваше предположение: ", 1, 101))
tries = 1

# Цикл отгадывания
while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    elif guess < the_number:
        print("Больше...")

    guess = int(ask_number("\nВаше предположение: ", 1, 101))
    tries += 1

print("\nПоздравляю! Вам удалось отгадать число!")
print("Вы затратили всего лишь", tries, "попытки(ок)!")

input("\nНажмите Enter, чтобы покинуть игру...")
