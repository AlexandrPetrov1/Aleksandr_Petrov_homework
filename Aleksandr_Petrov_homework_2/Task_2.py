# 2. Вводится трёхзначное число c клавиатуры. Необходимо вывести последние 2 символа через запятую (использую строки).
# Пример:
# входные данные: 189
# выходные данные: 8,9
# Подсказка: нужно перевести число в строку, потом выделить последние 2 символа.
str1 = str(int(input("Введите трехзначное число: ")))
print(f"Последние два символа: {str1[-2]},{str1[-1]}")