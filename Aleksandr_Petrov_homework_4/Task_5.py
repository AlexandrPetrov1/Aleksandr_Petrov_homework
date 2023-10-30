#5.	Вводится строка с пробелами.
# Разделите строку на слова и затем нужно вывести максимально по длине слово.
str1 = input("Введите строку ")
words = str1.split(" ")
max_el = words[0]
for i in words:
    if len(i) > len(max_el):
        max_el = i
print(f"Самое длинное слово: {max_el}")