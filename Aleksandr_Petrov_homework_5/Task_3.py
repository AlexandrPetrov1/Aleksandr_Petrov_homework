#3. Вводится n натуральных чисел с клавиатуры. Найти сумму чисел и максимальное их них.
n = int(input("Сколько чисел нужно ввести? "))
sum = 0
max = 1
i = 0
while i < n:
    num = int(input("Введите натуральное число: "))
    sum += num
    if num > max:
        max = num
    i += 1
print(f"Сумма введенных чисел равна {sum}, максимальное число: {max}")

