# 2. Случайным образом генерируется список из чисел. Создайте функцию, которая посчитает сумму элементов.
#
def sum_elem(x):
    sum1 = f"Сумма элементов: {sum(x)}"
    return sum1


import random
list1 = [random.randint(0,100) for i in range(10)]
print(list1)
print(sum_elem(list1))

