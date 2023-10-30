# 2. Создайте класс Фрукт, его свойствами будет: название фрукта, цвет и размер.
# - создайте метод, который будет выводить название и цвет фрукта
# - создайте абстрактный метод, который будет реализован в классах-потомках
# Также создайте от класса Фрукт несколько потомков для которых будет определено:
# страна от куда приехал фрукт (private)
# - создайте метод, который будет выводить название фрукта и страну от куда он приехал-
# придумайте любой метод, который бы реализовывал абстрактный метод класса-родителя

from abc import ABC, abstractmethod


class Fruit:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def print_name_and_color(self):
        print(f"Название фрукта: {self.name}, Цвет: {self.color}")

    @abstractmethod
    def print_name_and_origin_country(self):
        pass


class Apple(Fruit):
    def __init__(self, name, color, size, origin_country):
        super().__init__(name, color, size)
        self.__origin_country = origin_country

    def print_name_and_origin_country(self):
        print(f"Название фрукта: {self.name}, Страна происхождения: {self.__origin_country}")


class Banana(Fruit):
    def __init__(self, name, color, size, origin_country):
        super().__init__(name, color, size)
        self.__origin_country = origin_country

    def print_name_and_origin_country(self):
        print(f"Название фрукта: {self.name}, Страна происхождения: {self.__origin_country}")

    def custom_abstract_method(self):
        print("Вот такой абстрактный метод (0-o)")

apple = Apple("Яблоко", "Красное", "Среднее", "Россия")
banana = Banana("Банан", "Желтый", "Средний", "Эквадор")

apple.print_name_and_color()
apple.print_name_and_origin_country()

banana.print_name_and_color()
banana.print_name_and_origin_country()

banana.custom_abstract_method()