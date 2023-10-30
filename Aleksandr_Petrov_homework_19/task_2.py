# 2.	Вы разрабатываете систему управления магазином продуктов.
# У вас есть класс Product, представляющий продукт.
# Каждый продукт имеет имя, цену и количество на складе.
# Вам нужно реализовать методы для инициализации и обновления информации о продуктах.
#
# Ваша задача - создать методы класса Product, которые позволяют устанавливать начальные значения для продуктов и
# обновлять информацию о них. Кроме того, вы должны создать метод calculate_total_price, который вычисляет общую
# стоимость продуктов на складе.

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def prod_info(self):
    print(f"Продукт: {self.name}, цена: {self.price}, количество: {self.quantity}")

  def update_info(self, new_price, new_quantity):
    self.price = new_price
    self.quantity = new_quantity

  def calculate_total_price(self):
    return f'Общая стоимость {self.price * self.quantity}'


prod1 = Product("Яблоко", 5, 100)
prod1.prod_info()
prod1.update_info(7, 10)
prod1.prod_info()
prod1.calculate_total_price()

