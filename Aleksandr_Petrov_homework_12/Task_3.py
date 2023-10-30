#3)	В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
with open('file1.txt','r') as file:
        lines = file.readlines()
        line_count = len(lines)
        character_count = [len(line.strip()) for line in lines]

print("Количество строк в файле:", line_count)
print("Количество символов в каждой строке:")
for line_num, count in enumerate(character_count, start=1):
    print(f"Строка {line_num}: {count}")