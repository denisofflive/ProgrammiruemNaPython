# Проигранное сражение
# Демонстрирует тот самый ненавистный нам бесконечный цикл

print("Вашего героя окружила огромная армия троллей.")
print("Смрадными зелеными трупами врагов устланы все окрестные поля.")
print("Одинокий герой достает меч из ножен . готовясь к последней битве в своей жизни.\n")

Здоровье = 10
trolls = 0
damage = 3

while Здоровье != 0:
    trolls += 1
    Здоровье -= damage

    print("Взмахнув мечом, ваш герой истребляет злобного тролля, " \
          "но сам получает повреждений на", damage, "очков.\n")

print("Ваш герой доблестно сражался и убил", trolls, "троллей.")
print("Нo увы! Он пал на поле боя.")

input("\n\nНажмите Enter, чтобы выйти.")
