#1. Задан список, состоящий из чисел. Нужно вывести сумму нечетных чисел.
list1 = [1,12,14,65,28,6,7,19,96,53]
list2 = []
sum = 0
for num in list1:
    if num % 2 != 0:
        sum += num
        list2.append(num)
print(f"Из списка {list1} нечетные числа {list2} их сумма равна: {sum}")
