#3. Случайное число от 1 до 12 (номер месяца), использовать random.
#Нужно вывести какой это сезон года (зима, весна, лето, осень).
import random
month = random.randint(1,12)
print(f"месяц под номером {month}")
if month < 3 or month == 12:
    print("Сейчас зима")
elif month > 2 and month < 6:
    print("Сейчас весна")
elif month > 5 and month < 9:
    print("Сейчас лето")
else:
    print("Сейчас осень")



