# 2. Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
# выходные данные: {‘p’:1, ‘y’:1, ‘t’:2, ‘h’:1, ‘o’:1, ‘n’:1, ‘i’:1, ‘s’:1}
#
dict1 = {}

str1 = 'pythonist'
for i in str1:
    c = 0
    for j in str1:
        if i == j:
            c += 1
            dict1[i] = c
print(dict1)
