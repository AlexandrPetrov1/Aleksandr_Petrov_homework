# 3. Пользователь передает целое положительное число N, выведете на экран последовательность от 1 до N "ёлочкой"
# Пример: N = 16
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 12 13 15 16
N = int(input("Введите положительное число: "))
#
if N < 0:
    print("Введенное число отрицательное")
else:
    count = 1
    level = 1

    while count <= N:
        for i in range(level):
            if count > N:
                break
            print(count, end=" ")
            count += 1
        print()
        level += 1
