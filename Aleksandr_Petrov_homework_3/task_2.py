# 2. Вводится число, как строка, с клавиатуры.
# Необходимо проверить делится ли оно на 5 и вывести «Yes» или «No».
# Также проверить делится ли оно на 4 и вывести «Yes» или «No».
# Подсказка: Число делится на 5, если оканчивается на 0 или 5. Число делится на 4,
# если две последние его цифры — нули или образуют число, которое делится на 4.
str1 = input("Введите число: ")
if str1[0] == "0" and len(str1) > 1:
    print("некорректно введено число")
elif str1.isdigit():                          #проверяем введено ли число
        if str1[-1] == "5" or str1[-1] == "0":
            print(f"Число {str1} делится на 5")
        else:
            print(f"Число {str1} не делится на 5")
        if str1[(len(str1)-2):len(str1)] == "00" or int(str1[(len(str1)-2):len(str1)]) % 4 == 0:
            print(f"Число {str1} делится на 4")
        else:
            print(f"Число {str1} не делится на 4")
else:
    print("Число введенно не правильно")