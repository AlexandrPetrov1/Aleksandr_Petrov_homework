# 4. Вводится список чисел. Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов.
# Пример:
# входные данные:
# Введите список: 1 2 3 4 5
# выходные данные: 0
# Пример:
# входные данные:
# Введите список: 1 5 1 5 1
# выходные данные: 2
numbers = input("Введите список: ")
list1 = numbers.split()
count = 0
for i in range(1, len(list1)-1):
    if int(list1[i]) > int(list1[i-1]) and int(list1[i]) > int(list1[i+1]):
        count += 1

print(f"Элементов которые больше двух своих соседей {count}")