# 4.  Необходимо создать словарь, где ключами будут выступать числа от 0 до n
# (n задается с клавиатуры), а значениями будут случайные числа из диапазона от 100 до 200.
import random
n = int(input('Введите число: '))
dict1 = {key : random.randint(100,200) for key in range(n+1)}
print(f"Словарь {dict1}")