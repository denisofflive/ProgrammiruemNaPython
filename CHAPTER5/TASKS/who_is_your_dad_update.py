"""
Доработайте программу "Кто твой папа?" так, чтобы можно было,
введя имя человека, узнать, кто его дед. Программа должна
по-прежнему пользоваться словарем с парами "сын-отец".
Подумайте, как включить в этот словарь несколько
поколений.
"""
menu = ("""
        1 - Поиск деда человека по имени
        2 - Изменение данных
        3 - Удаление данных
        4 - Добавить новые данные
        5 - Выход
""")

family = {"Bob": {"Sam": "Ben"}, "Luke": {"Anakin": "The Force"},
          "Jon Snow": {"Rhaegar Targaryen": "Aerys II Targaryen "},
          "Robb Stark": {"Ned Stark": "Rickard Stark "}}

print(f"Список пар {family}")

choice = None
son = ""
father = ""
dad = []
g_dad = ''
while choice != 5:
    print(menu)
    choice = int(input("Выберите пункт меню: "))

    # Поиск отца человека по имени.
    if choice == 1:
        son = str(input("Введите имя человека: "))
        if son in family:
            dad = list(family[son].keys())
            g_dad = family[son][dad[0]]
            print("Родителем человека по имени {} является {}, а его дедом {}". \
                  format(son, dad[0], g_dad))
        else:
            print("Ошибка, такого человека нет в базе данных")

    # Изменение данных
    elif choice == 2:
        son = str(input("Введите имя человека: "))
        if son in family:
            father = str(input("Напиши новое имя его отца: "))
            g_dad = str(input("Напиши новое имя его деда: "))
            family[son] = {father: g_dad}
            print("Родителем человека по имени {} является {}, а его дедом {}". \
                  format(son, father, family[son][father]))
            print(f"Список пар {family}")
        else:
            print("Ошибка, такого человека нет в базе данных")

    # Удаление данных.
    elif choice == 3:
        son = str(input("Введите имя человека: "))
        if son in family:
            del family[son]
            print("Запись удалена")
            print(f"Список пар {family}")
        else:
            print("Ошибка, такого человека нет в базе данных")

    # Добавить новые данные
    elif choice == 4:
        son = str(input("Введите имя человека: "))
        if son in family:
            print("Такая запись уже существует")
        else:
            father = str(input("Напиши имя его отца: "))
            g_dad = str(input("Напиши новое имя его деда: "))
            family[son] = {father: g_dad}
            print("Добавлено в базу данных")
            print(f"Список пар {family}")

    # Выход.
    elif choice == 5:
        print("До свиданья!")
