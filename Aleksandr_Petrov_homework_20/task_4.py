# 4) Вы разрабатываете систему для управления университетскими курсами и студентами.
# У вас есть базовый класс Course (курс), представляющий учебный курс, и класс Student (студент), представляющий учащегося.
#
# Course имеет следующие атрибуты:
# course_code (код курса)
# course_name (название курса)
# credit_hours (количество кредитных часов)
#
# Student имеет следующие атрибуты:
# student_id (идентификационный номер студента)
# name (имя студента)
# enrolled_courses (список курсов, на которые студент записан)
# У всех студентов должен быть метод enroll_course, который позволяет записать студента на курс.
#
# У курсов должен быть метод add_student, который позволяет добавить студента на курс.
#
# У класса Course и Student должен быть метод get_info, который возвращает информацию о курсе или студенте соответственно.
#
# Создайте класс University, который хранит список курсов и студентов и предоставляет методы для создания новых курсов,
# записи студентов на курсы и получения информации о курсах и студентах.
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_info(self):
        return f"Код курса: {self.course_code}, название курса: {self.course_name}, количество часов: {self.credit_hours}"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def get_info(self):
        list_course = ', '.join([course.course_name for course in self.enrolled_courses])
        return f"ID студента: {self.student_id}, Имя: {self.name} Посещаемые курсы: {list_course}"

class University:
    def __init__(self):
        self.courses = []
        self.students = []

    def create_course(self, course_code, course_name, credit_hours):
        course = Course(course_code, course_name, credit_hours)
        self.courses.append(course)

    def create_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def enroll_student(self, student_id, course_code):
        student = None
        for student in self.students:
            if student.student_id == student_id:
                break
        if student is None:
            student = None

        course = None
        for course in self.courses:
            if course.course_code == course_code:
                break
        if course is None:
            course = None

        if student and course:
            student.enroll_course(course)
            course.add_student(student)

    def get_course_info(self, course_code):
        course = next((course for course in self.courses if course.course_code == course_code), None)
        if course:
            return course.get_info()
        else:
            return "Курс не найден."

    def get_student_info(self, student_id):
        student = next((student for student in self.students if student.student_id == student_id), None)
        if student:
            return student.get_info()
        else:
            return "Студент не найден."



university = University()


university.create_course("A123", "Python", 300)
university.create_course("B321", "Java", 150)


university.create_student(1, "Иванов Иван")
university.create_student(2, "Петров Петр")


university.enroll_student(1, "A123")
university.enroll_student(1, "B321")
university.enroll_student(2, "B321")

print(university.get_course_info("A123"))
print(university.get_course_info("B321"))

print(university.get_student_info(1))
print(university.get_student_info(2))