# 2.	 Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на
# три колонки: наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт.
# (целое число). Напишите программу, подсчитывающую общую стоимость заказа.
prices = 0
with open('prices.txt', 'r') as file:
    for line in file:
        name, kol, price = line.strip().split('\t')
        kol_price = int(kol)*int(price)
        prices += kol_price
        print(f"Цена за {name} = {kol_price}")
print(f"Стоимость всех товаров: {prices}")