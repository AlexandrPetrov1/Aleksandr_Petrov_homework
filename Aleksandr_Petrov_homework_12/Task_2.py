#2)	Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка.
with open('file1.txt','w') as file:
    while True:
        word = input("Введите слово:")
        file.write(word)
        file.write('\n')
        if len(word) == 0:
            print('Вы ввели пустую строку!')
            break
