# 3.	Вам предоставляется CSV-файл, содержащий данные о продажах различных товаров.
# Каждая строка файла содержит информацию о конкретной продаже: название товара,
# количество проданных единиц и цена за единицу.
# Ваша задача - написать программу, которая считывает данные из файла и вычисляет общую сумму продаж.
import csv
prices = 0
with open('input.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for elem in reader:
        prices += int(elem[1]) * int(elem[2])
        print(f"Сумма за {elem[0]} = {int(elem[1]) * int(elem[2])}")
print(f"Общая сумма продаж {prices}")
