#4. Дана строка, нужно выделить все четные символы, потом все нечетные. Затем соединить в одну строку и вывести.
str1 = "qwerty123"
str2 = str1[::2]
str3 = str1[1::2]
print(f"Четные символы: {str3}, нечетные символы {str2}, строка: {str3 + str2}")
