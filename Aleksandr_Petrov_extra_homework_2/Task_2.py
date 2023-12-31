# 2.  Политическая жизнь одной страны очень оживленная. В стране действует K политических партий,
# каждая из которых регулярно объявляет национальную забастовку.
# Дни, когда хотя бы одна из партий объявляет забастовку, при условии, что это не суббота или воскресенье
# (когда и так никто не работает), наносят большой ущерб экономике страны.
# i-я партия объявляет забастовки строго каждые bi дней, начиная с дня с номером ai.
# То есть i-я партия объявляет забастовки в дни ai, ai+bi, ai+2bi и т.д.
# Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.
# В календаре страны N дней, пронумерованных от 1 до N.
# Первый день года является понедельником, шестой и седьмой дни недели — выходные,
# неделя состоит из семи дней.
# Программа получает на вход число дней в году N и число политических партий K.
# Далее идет K строк, описывающие графики проведения забастовок. i-я строка содержит числа ai и bi.
# Выведите единственное число: количество забастовок, произошедших в течение года.
# Пример входных данных:
# 19 3
# 2 3
# 3 5
# 9 8
# Выходные данные:
# 8
# Примечание. Первая партия объявляет забастовки в дни 2, 5, 8, 11, 14, 17.
# Вторая партия объявляет забастовки в дни 3, 8, 13, 18. Третья партия — в дни 9 и 17.
# Дни номер 6, 7, 13, 14 являются выходными. Таким образом, общенациональные
# забастовки пройдут в дни 2, 3, 5, 8, 9, 11, 17, 18.

def count_strike_days(N, K, strikes):
    strike_count = 0
    weekend_days = [6, 7]  # выходные дни
    for day in range(1, N + 1):
        if (day % 7 and day % 6) not in weekend_days:  # проверяем, не является ли текущий день выходным
            for i in range(K):
                if (day - strikes[i][0]) % strikes[i][1] == 0:
                    # если текущий день соответствует графику проведения забастовок для i-й партии
                    strike_count += 1
                    break  # прерываем цикл, чтобы избежать повторного подсчета забастовок
    return f"Kоличество забастовок, произошедших в течение года: {strike_count}"

# чтение входных данных
N, K = map(int, input('Введите число дней в году N и число политических партий K: ').split())
strikes = []
for _ in range(K):
    a, b = map(int, input("Введите графики проведения забастовок: ").split())
    strikes.append((a, b))

# вызов функции и вывод результата
print(count_strike_days(N, K, strikes))