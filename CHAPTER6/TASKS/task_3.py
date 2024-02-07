# Доработайте новую версию игры «Отгадай число» (которую вы создали, решая
# предыдущую задачу) так, чтобы основная часть программы стала функцией main().
# Для того чтобы игра началась, не забудьте вызвать эту функцию глобально.

import random

print("\t\tДобро пожаловать в игру 'Отгадай число'!")
print("Компьютер загадал натуральное число из диапазона от 1 до 100.")
print("Попытайтесь отгадать его зха минимальное число попыток.\n")

the_number = random.randint(1, 100)

def ask_number(question, low, high,):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def main():
    guess = int(ask_number("Ваше предположение: ", 1, 101))
    tries = 1

    while guess != the_number:
        if guess > the_number:
            print("Меньше...")
        elif guess < the_number:
            print("Больше...")

        guess = int(ask_number("\nВаше предположение: ", 1, 101))
        tries += 1

    print("\nПоздравляю! Вам удалось отгадать число!")
    print("Вы затратили всего лишь", tries, "попытки(ок)!")

main()
input("\nНажмите Enter, чтобы покинуть игру...")
