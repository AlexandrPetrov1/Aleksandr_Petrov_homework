# 3. Необходимо заполнить список ста нулями, кроме первого и последнего элементов,
# которые должны быть равны единице
list1 = []
for i in range(100):
    if len(list1) == 0:
        list1.append(1)
    elif len(list1) < 99:
        list1.append(0)
    else:
        list1.append(1)
print(f"Список: {list1}")
print(f"Длина списка: {len(list1)}")
