# 4. *Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета (1- красный, 2 - черный).
# Пользователю дается 5 попыток угадать номер и цвет. Добавьте дополнительно комментарии для пользователя.
# В случае неудачи (то есть за 5 попыток не угадал) вывести на экран правильную комбинацию.
# Пример:
# входные данные:
# Введите номер: 4
# Введите цвет: черный
# выходные данные: Ваш номер больше загаданного, цвет угадан
# входные данные:
# Введите номер: 2
# Введите цвет: черный
# выходные данные: Ваш номер меньше загаданного, цвет угадан
# входные данные:
# Введите номер: 3
# Введите цвет: черный
# выходные данные: Номер угадан, цвет угадан
import random
num1 = random.randint(1,10)
color1 = random.randint(1,2)
i = 5
while i >= 0:
    num2 = int(input("Введите число от 1 до 10: "))
    color2 = int(input("Введите номер цвет (1 - красный, 2 - черный): "))
    if num2 < 1 or num2 > 10 or color2 < 1 or color2 > 2:
        print("Данные введены неверно")
        break
    if num2 > num1 and color2 != color1:
        print("Ваш номер больше загаданного, цвет не угадан")
    elif num2 < num1 and color2 != color1:
        print("Ваш номер меньше загаданного, цвет не угадан")
    elif num2 > num1 and color2 == color1:
        print("Ваш номер больше загаданного, цвет угадан")
    elif num2 < num1 and color2 == color1:
        print("Ваш номер меньше загаданного, цвет угадан")
    else:
        print("Номер угадан, цвет угадан")
        break
    i -= 1
    print(f"У вас осталось {i} попыток")
    if i == 0:
        print(f"Вы не угадали. Загаданный номер {num1}, а номер цвета {color1}")
        break
