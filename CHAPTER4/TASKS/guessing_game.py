"""
Создайте игру «Отгадайка», в которой компьютер выбирает какое-либо слово,
а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове,
и дает пять попыток узнать, есть ли какая-либо буква в слове,
причем программа может отвечать только «Да» и «Heт».
Вслед за тем игрок должен попробовать отгадать слово.
"""

import random

print('Игра "Отгадайка".\n Я загадаю слово, а ты будешь его угадывать.\n \
Я скажу тебе, сколько букв в этом слове. \n \
И еще ты можешь 5 раз узнать у меня, есть ли какая-либо буква в этом слове.')
input('Если готов играть, нажми Entr')
slova = ('сосиска',
         'крокодил',
         'медведь',
         'завтрак',
         'компьютер')

slovo = random.choice(slova)
print('В этом слове', len(slovo), 'букв')
print('Теперь ты можешь 5 раз спросить меня, есть ли какая-то буква в этом слове?\n')
for _ in range(5):
    bukva = input('Напиши букву, которую хочешь проверить?')
    if bukva in slovo:
        print('Да')
    else:
        print('Нет')
otgadka = input('Какое слово было загадано?\n')
if otgadka == slovo:
    print('Ура, ты угадал!')
else:
    print('Нет, попробуй в другой раз')

input("\n\nНажмите Enter, чтобы выйти.")
