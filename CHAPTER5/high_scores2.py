# Рекорды 2.0
#  Демонстрирует вложенные последовательности

scores = []

choice = None
while choice != "0":

    print(
        """
    Рекорды 2. О 
    О - Выйти 
    1 - Показать рекорды 
    2 - Добавить рекорд 
        """
    )

    choice = input("Baш выбор: ")
    print()

    # выход
    if choice == "0":
        print("До свидания.")

    # вь1вод таблицы рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # в списке остается только 5 рекордов


    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)

input("\n\nНажмите Enter, чтобы выйти.")
