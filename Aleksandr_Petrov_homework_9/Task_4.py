# 4. * Создается два кортежа, размером 10 элементов, из случайных чисел из диапазона от 15 до 55.
# Нужно найти в каждом кортеже максимальный элемент и сравнить их, вывести тот, что больше.
# Если максимальные элементы равны, то сравнивать минимальные элементы.
import random
tuple1 = tuple([random.randint(15,55) for i in range(10)])
tuple2 = tuple([random.randint(15,55) for i in range(10)])
print(tuple1)
print(tuple2)
if max(tuple1) > max(tuple2):
    print(f"Максимальный элемент из двух картежей: {max(tuple1)}")
elif max(tuple1) < max(tuple2):
    print(f"Максимальный элемент из двух картежей: {max(tuple2)}")
else:
    if min(tuple1) > min(tuple2):
        print(f"Минимальный элемент из двух картежей: {min(tuple2)}")
    else:
        print(f"Минимальный элемент из двух картежей: {min(tuple1)}")
