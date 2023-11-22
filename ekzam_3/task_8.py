#8) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента. Класс студен описан следующим образом:
# class Student:
# def __init__(self, name, money):
# 	self.name = name
# 	self.money = money

class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money


student1 = Student("Иван", 1000)
student2 = Student("Мария", 1500)
student3 = Student("Петр", 800)

# Подсчет денег каждого студента
print(f"{student1.name} имеет {student1.money} денег.")
print(f"{student2.name} имеет {student2.money} денег.")
print(f"{student3.name} имеет {student3.money} денег.")
print(f"Общая сумма денег: {student1.money + student2.money + student3.money}")