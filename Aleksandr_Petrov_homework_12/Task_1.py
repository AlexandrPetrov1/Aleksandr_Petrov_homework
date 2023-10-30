#1)	Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длины.
numbers = []
words = []
with open('file.txt') as file:
    for line in file:
        element = line.strip()
        if element.isdigit():
            numbers.append(int(element))
        else:
            words.append(element)
words_len = sorted(words, key=lambda x:len(x))
numbers_len = sorted(numbers)
print(f"Результат: {numbers_len+words_len}")

