#1. Вводится два числа с клавиатуры. Выведите диапазон между этими двумя числами.
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
if num1 > num2:
    i = num2
    while i <= num1:
        print(i)
        i += 1
else:
    i = num1
    while i <= num2:
        print(i)
        i += 1

