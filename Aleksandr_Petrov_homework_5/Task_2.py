#2. Выведите все нечетные числа, которые делятся на 3 в диапазоне от 100 до 250.
num = 101
while num < 251:
    if num % 2 != 0 and num % 3 == 0:
        print(num)
    num += 2
