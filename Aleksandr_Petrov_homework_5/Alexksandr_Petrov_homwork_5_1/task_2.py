# 2. Вводятся десять натуральных чисел больше 2. Посчитать, сколько среди них простых чисел.
k = 1
i = 0
list = []
while k < 11:
    num = int(input("Введите натуральное число > 2 : "))
    
    print(f"Вы ввели {k}-ое число: {num}")
    if num == 3:
        list.append(num)
        i += 1
    elif num > 3:
        j = 2
        f = True
        while j * j <= num:
            if num % j == 0:
                f = False
                break
            else:
                j += 1
        if f:
            list.append(num)
            i += 1
    k += 1
print(f"Простые числа: {list},  их количество: {i}")

