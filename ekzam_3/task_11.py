# 11) Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# apple = Apple("sort", [a,b,c], 120, "apple")
# apple.clear()
# >>"apple очищен"

class Fruit:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

class Orange(Fruit):
    def clear(self):
        return f"{self.name} очищен"

class Apple(Fruit):
    def cut(self):
        return f"{self.name} порезан"

class Mandarin(Fruit):
    def clear(self):
        return f"{self.name} очищен"

class Banana(Fruit):
    def __init__(self, sort, vitamins, price, name, potassium):
        super().__init__(sort, vitamins, price, name)
        self.potassium = potassium

    def clear(self):
        return f"{self.name} очищен"


orange = Orange("апельсин", ["витамин С"], 50, "апельсин")
apple = Apple("голден", ["витамин A", "витамин C"], 70, "яблоко")
mandarin = Mandarin("мандарин", ["витамин С"], 40, "мандарин")
banana = Banana("банан", ["витамин B6", "витамин C"], 60, "банан", "300 мг")

print(orange.clear())
print(apple.cut())
print(mandarin.clear())
print(banana.clear())
print(f"Количество калия в банане: {banana.potassium}")