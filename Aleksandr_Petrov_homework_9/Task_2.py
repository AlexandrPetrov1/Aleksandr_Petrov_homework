#2. Имеются два списка, сгенерированные случайным образом.
# Добавьте в конец первого списка все элементы второго списка.
import random
list1 = list([random.randint(0,5) for i in range(5)])
list2 = list([random.randint(0,5) for i in range(5)])
print(f"Первый список {list1}")
print(f"Второй список {list2}")
print(f"Cписок из двух: {list1 + list2}")
