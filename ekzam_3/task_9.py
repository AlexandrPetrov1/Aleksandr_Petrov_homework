# 9) Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (список из пяти элементов).
# Создать класс School:
# Добавить возможно для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Student:
    def __init__(self, name, group_number, grades):
        self.name = name
        self.group_number = group_number
        self.grades = grades

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def excellent_students(self):
        excellent = [student for student in self.students if all(grade in [5, 6] for grade in student.grades)]
        return [(student.name, student.group_number) for student in excellent]

    def find_students_by_group(self, group_number):
        return [(student.name, student.group_number) for student in self.students if student.group_number == group_number]

    def potential_scholars(self):
        potential_scholars = [student for student in self.students if sum(student.grades) / len(student.grades) >= 7]
        return [(student.name, student.group_number) for student in potential_scholars]


# Пример использования
student1 = Student("Иванов И.И.", 101, [5, 6, 7, 6, 5])
student2 = Student("Петров П.П.", 102, [6, 6, 6, 6, 6])
student3 = Student("Сидоров С.С.", 101, [7, 8, 9, 7, 8])

school = School()
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

print("Отличники:")
print(school.excellent_students())

print("Студенты группы 101:")
print(school.find_students_by_group(101))

print("Претенденты на автомат:")
print(school.potential_scholars())