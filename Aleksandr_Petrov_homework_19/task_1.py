# 1.	Создайте класс Vector, представляющий вектор в трехмерном пространстве.
# Определите магические методы для арифметических операторов (+, -, *, /), чтобы можно было
# выполнять операции над векторами.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other): # правило параллелограмма
        global a,b,d
        a = ((self.x ** 2) + (self.y ** 2) + (self.z ** 2))**0.5 # первый вектор
        b = ((other.x ** 2) + (other.y ** 2) + (other.z ** 2))**0.5 # второй вектор
        d = (((self.x - other.x)**2)+((self.y - other.y)**2)+((self.z - other.z)**2))**0.5 # вторая диагональ
        summa = ((2 * (a**2 + b**2)) - d**2)**0.5 # сумма векторов (диагональ параллелограмма)
        return f"Сумма векторов равна: {summa}"

    def __sub__(self, other):
        c = (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2)) ** 0.5 # Вычитание вектора по координатам
        return f"Разность векторов {c}"

    def __mul__(self, other):
        a = (((self.x ** 2) + (self.y ** 2) + (self.z ** 2))**0.5) * other # Произведение вектора на число
        return f"Произведение вектора на число {other}, равно {a}"

    def __truediv__(self, other):
        a = (((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5) / other # деление вектора на число
        return f"Деление вектора на число {other}, равно {a}"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 2
v6 = v2 * 3
v7 = v1 / 2
print(v3)
print(v4)
print(v5, v6)
print(v7)
print("Длина векторов",a,b)
