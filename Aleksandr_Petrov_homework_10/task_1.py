# 1. Даны два списка одинаковой длины.
# Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — значениями словаря.
#
list1 = [1,2,3,4,5]
list2 = ['cat', 'dog', 'wolf', 'horse', 'panda']
dict1 = dict(zip(list1,list2))
print(f"Словарь из двух списков: {dict1}")