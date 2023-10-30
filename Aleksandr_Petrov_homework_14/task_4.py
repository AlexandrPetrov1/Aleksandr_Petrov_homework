# 4. Создайте калькулятор. Пользователь вводит два числа и операцию (+, - , *, **, /).
# Создайте разные лямба-функции для всех операций. Выведите итог.
#

add = lambda x, y: x + y

subtract = lambda x, y: x - y

multiply = lambda x, y: x * y

power = lambda x, y: x ** y

divide = lambda x, y: x / y

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, **, /): ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "**":
    result = power(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Неверная операция"

print("Результат:", result)