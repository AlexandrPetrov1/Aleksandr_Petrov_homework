# ) Задача: покупка дома
# 	Описание классовой структуры
# Есть Человек, характеристиками которого являются:
# 1.	Имя
# 2.	Возраст
# 3.	Наличие денег
# 4.	Наличие собственного жилья
# Человек может:
# 1.	Предоставить информацию о себе
# 2.	Заработать деньги
# 3.	Купить дом
# Также же есть Дом, к свойствам которого относятся:
# 1.	Площадь
# 2.	Стоимость
# Для Дома можно:
# 1.	Применить скидку на покупку
# Также есть Небольшой Типовой Дом, обязательной площадью 40м2.
# Задание
# Класс Human
# 1.	Создайте класс Human.
# 2.	Определите для него два статических атрибута: default_name и default_age.
# 3.	Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя атрибута default_name и default_age.
# В методе __init__() определите четыре атрибута: Публичные - name и age. Приватные - money и house.
# 4.	Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# 5.	Реализуйте справочный статический метод default_info(), который будет выводить статические атрибуты
# default_name и default_age.
# 6.	Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов
# данный метод принимает объект дома и его цену.
# 7.	Реализуйте метод earn_money(), увеличивающий значение свойства money.
# 8.	Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и
# совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на
# дом и размер скидки
# Класс House
# 1.	Создайте класс House
# 2.	Создайте метод __init__() и определите внутри него два атрибута: _area и _price. Свои начальные значения они
# получают из параметров метода __init__()
# 3.	Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом
# данной скидки.
# Класс SmallHouse
# 1.	Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2.	Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# Тесты
# 1.	Вызовите справочный метод default_info() для класса Human()
# 2.	Создайте объект класса Human
# 3.	Выведите справочную информацию о созданном объекте (вызовите метод info()).
# 4.	Создайте объект класса SmallHouse
# 5.	Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# 6.	Поправьте финансовое положение объекта - вызовите метод earn_money()
# 7.	Снова попробуйте купить дом
# 8.	Посмотрите, как изменилось состояние объекта класса Human

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price


    def final_price(self, discount):
        return self._price - discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


class Human:
    default_name = "Иван"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._house = None

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Деньги: {self._money}, Дом: {self._house}")

    @staticmethod
    def default_info():
        print(f"Имя по умолчанию: {Human.default_name}, Возраст по умолчанию: {Human.default_age}")

    def make_deal(self, house, price):
        if self._money >= price:
            self._money -= price
            self._house = house
            print("Поздравляем с покупкой дома!")
        else:
            print("У вас недостаточно денег для покупки этого дома.")

    def earn_money(self, amount):
        self._money += amount

    def buy_house(self, house, discount):
        price_with_discount = house.final_price(discount)
        self.make_deal(house, price_with_discount)




Human.default_info()

person = Human()
person.info()

small_house = SmallHouse(50000)
person.buy_house(small_house, 10000)
person.earn_money(60000)
person.buy_house(small_house, 10000)
person.info()