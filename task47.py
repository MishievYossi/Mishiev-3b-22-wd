"""
Напишите программу, которая запрашивает у пользователя число и выводит его
квадрат. Если пользователь вводит некорректные данные (например, символы вместо
числа), программа должна выводить сообщение "Ошибка" и прекращать работу.
"""


input_number = input("Введите число: ")
try:
    arg = int(input_number)
except ValueError:
    print("Ошибка")
else:
    print(arg * arg)
