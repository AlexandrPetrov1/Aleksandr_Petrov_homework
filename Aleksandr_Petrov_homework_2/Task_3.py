# 3. Дана строка с пробелами. Выведите последние слово, затем, проверьте состоит ли оно только из букв.
str1 = "qwerty 1234 ytrewq1 ,l, gvyv"
str2 = str1[(str1.rindex(" ")+1):]
print(f"Последнее слово: {str2}")
print(f"Состоит ли оно только из букв? {str2.isalpha()}")