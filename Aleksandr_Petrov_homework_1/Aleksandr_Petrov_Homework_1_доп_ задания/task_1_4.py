# 4. Улитка ползет по вертикальному шесту высотой H метров,
# поднимаясь за день на A метров, а за ночь спускаясь на B метров.
# Вводится H, A, B с клавиатуры, на выходе вывести
# на какой день улитка доползет до вершины шеста.
H = int(input("Введите высоту шеста: "))
A = float(input("Введите на сколько метров улитка поднимается за день: "))
B = float(input("Введите на сколько метров улитка спускается за ночь: "))
print(f"Улитка поднимется по вертикальному шесту высотой {H} метров на {round(H / (A - B))} день")