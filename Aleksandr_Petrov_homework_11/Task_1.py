# 1. Даны два множества, состоящие из чисел.
# Необходимо найти их объединение, пересечение, разность и симметрическую разность (через два обозначения).
set1 = {i for i in range(10)}
set2 = {i for i in range(2,13)}
print(f"Объединение: {set1.union(set2)}")
print(f"Пересечение: {set1.intersection(set2)}")
print(f"Разность: {set1.difference(set2)}")
print(f"Симметрическая разность: {set1.symmetric_difference(set2)}")
