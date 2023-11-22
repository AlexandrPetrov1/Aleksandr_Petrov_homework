# 1)	Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# ●	Ура, можно построить треугольник!
# ●	С отрицательными числами ничего не выйдет!
# ●	Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            self.result = "С отрицательными числами ничего не выйдет!"
        elif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            self.result = "Ура, можно построить треугольник!"
        else:
            self.result = "Жаль, но из этого треугольник не сделать."

    def is_triangle(self):
        return self.result

triangle1 = TriangleChecker(3, 4, 5)
print(triangle1.is_triangle())

triangle2 = TriangleChecker(1, 1, 3)
print(triangle2.is_triangle())

triangle3 = TriangleChecker(-1, 2, 4)
print(triangle3.is_triangle())  