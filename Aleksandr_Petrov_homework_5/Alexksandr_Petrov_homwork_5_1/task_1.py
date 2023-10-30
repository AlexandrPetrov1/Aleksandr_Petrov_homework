# 1. Вывести на экран, из каких простых множителей состоит введенное натуральное число.
num = int(input("Введите натуральное число: "))
num1 = num
list1 = []
i = 2
while i * i <= num:
    if num % i == 0:
        list1.append(i)
        num //= i
    else:
        i += 1
if num > 1:
    list1.append(num)
print(f"Число {num1} состоит из простых множителей {list1}")
