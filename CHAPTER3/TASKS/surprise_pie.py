"""
Напишите программу- симулятор пирожка с «сюрпризом»,
которая бы при запуске отображала один из
пяти различных «Сюрпризов», выбранный случайным образом.
"""
import random

print("\t\t\t\tЗдравствуйте!")
print("Вы, как постоянный клиент, получаете пирожок с секретной начинкой!")
print("У нас 5 секретных начинок, и мы не знаем какая вам достанется. Удачи!\n")

# Создаем случайные числа из диапазона 1 - 5
get_surprise = random.randint(1, 5)

# Создаем условия от 1 до 5 включительно под каждый сюрприз
if get_surprise == 1:
    print('В пирожке нет сюрприза, но он очень вкусный!')
elif get_surprise == 2:
    print('Вы нашли монетку в пирожке!')
elif get_surprise == 3:
    print('В пирожке лежит маленькая игрушка!')
elif get_surprise == 4:
    print('Пирожок оказался с победным билетом!')
elif get_surprise == 5:
    print('В пирожке находится записка с пожеланием удачи!')

else:
    print('Что такое пирожок ?')

input("\n\nНажмите Enter, чтобы выйти.")
