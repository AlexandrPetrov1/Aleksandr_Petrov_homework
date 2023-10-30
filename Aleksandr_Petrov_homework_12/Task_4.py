#4)	(try-except) Напишите программу, которая запрашивает ввод строки.
# Если в ней есть хотя бы символ - число, то выведите ошибку и заново попросите ввести строку.
# Если все символ буквы, то выведите количество буквы «а».
while True:
    try:
        str1 = input("Введите строку: ")
        if any(char.isdigit() for char in str1):
            raise ValueError
        else:
            count = str1.count('a')
            print(f"Количество символов 'а' в строке: {count}")
            break
    except ValueError:
        print("Ошибка: в строке есть цифры")
