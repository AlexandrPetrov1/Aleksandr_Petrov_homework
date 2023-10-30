#3.	Вводится строка с клавиатуры.
# Если в ней есть повторение слов, то выведите "Yes", в противном случае "No"
str1 = input("Введите строку ")
words = str1.split(" ")
unique_words = []

for word in words:
    if word in unique_words:
        print("Yes")
        break
    unique_words.append(word)

else:
    print("No")
