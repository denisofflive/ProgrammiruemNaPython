""" Напишите программу «Щедрый посетитель»,
в окно которой пользователь сможет ввести сумму счета за обед
в ресторане. Программа должна выводить два значения:
 чаевые из расчета 15 и 20 % от указанной суммы."""

# Имя клиента
client_name = input("Напомните, как вас зовут: ")
# Сумма счета за обед
score = int(input("Введите сумму счета за обед: "))

gratuity15 = score * 0.15
input("\nЕсли хотите узнать 15% чаевые за обед, нажмите Enter")
print(gratuity15)

gratuity20 = score * 0.20
input("\nЕсли хотите узнать 20% чаевые за обед, нажмите Enter")
print(gratuity20)

input("\nНажмите Enter, чтобы выйти.")
