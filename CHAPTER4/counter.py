# Считалка
# Демонстрирует использование функции range(J

print("Посчитаем:")
# перебор чисел начинается с нуля и до 9 включительно, 10 не входит
for i in range(10):
    print(i, end=" ")

print("\n\nПеречислим кратные пяти:")
# 0 - это начало, 50 - конец(посчитает до 45 включительно) 5 - интервал
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nПосчитаем в обратном порядке:")
# Посчитает в обратном порядке от 10 до 0 по одному интервалу
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nНажмите Enter, чтобы выйти.")