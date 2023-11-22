# 6) Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов:
# getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения
# данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного
# студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber
# позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять
# экземпляров класса Student, установить им разные имена, возраст и номер группы.
class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

student1 = Student('Alice', 20, '11B')
student2 = Student('Bob', 19, '11A')
student3 = Student('Eva', 21, '10B')
student4 = Student()
student5 = Student()

print(student1.getName(), student1.getAge(), student1.getGroupNumber())
print(student2.getName(), student2.getAge(), student2.getGroupNumber())
print(student3.getName(), student3.getAge(), student3.getGroupNumber())
print(student4.getName(), student4.getAge(), student4.getGroupNumber())
print(student5.getName(), student5.getAge(), student5.getGroupNumber())