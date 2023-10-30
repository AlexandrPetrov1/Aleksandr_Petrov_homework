# 4. *Вводитcя четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
# сначала для первой клетки, потом для второй клетки на шахматной доске.
# Ладья ходит по горизонтали или вертикали.
# Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Пример:
# входные данные:
# Введите номер столбца: 4
# Введите номер строки: 4
# Введите номер столбца: 5
# Введите номер строки: 5
# выходные данные: No
# * Дополнительно можно сделать для ферзя (ходит по диагонали, горизонтали или вертикали) и коня (ходит буквой Г).
stolb1 = int(input("Введите номер столбца от 1 до 8: "))
stroka1 = int(input("Введите номер строки от 1 до 8: "))
stolb2 = int(input("Введите номер столбца от 1 до 8: "))
stroka2 = int(input("Введите номер строки от 1 до 8: "))
if stolb1 < 1 or stolb1 > 8 or stroka1 < 1 or stroka1 > 8 \
    or stolb2 < 1 or stolb2 > 8 or stroka2 < 1 or stroka2 > 8:
    print("Неверно введены координаты")
else:
    if stolb1 == stolb2 or stroka1 == stroka2:
        print(f"Ладья может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")
    else:
        print(f"Ладья не может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")
    if stolb1 == stolb2 or stroka1 == stroka2 or (stolb2 - stolb1 == stroka2 - stroka1):
         print(f"Ферзь может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")
    else:
         print(f"Ферзь не может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")
    if (stolb1 + - 2 == stolb2 or stolb1 + - 2 == stolb2) and (stroka1 + - 1 == stroka2 or stroka1 + - 1 == stroka2) \
            or (stolb1 + 1 == stolb2 or stolb1 - 1 == stolb2) and (stroka1 + 2 == stroka2 or stroka1 - 2 == stroka2):
        print(f"Конь может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")
    else:
        print(f"Конь не может попасть из клетки ({stolb1},{stroka1}) в клетку ({stolb2},{stroka2}) за один ход")