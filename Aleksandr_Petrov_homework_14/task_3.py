# 3. Создайте функцию, которая будет заполнять список числами в диапазоне, указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
# Вывести список. Подсказка: список сделать global.
#
import random
def list_elem(a,b):
    global l
    l = [random.randint(a,b) for i in range(10)]

num1 = int(input('Введите начало диапазона списка: '))
num2 = int(input('Введите конец диапазона списка: '))
list_elem(num1,num2)
print(l)