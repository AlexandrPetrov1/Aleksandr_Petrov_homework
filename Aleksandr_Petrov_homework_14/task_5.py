# 5. Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае # (использовать рекурсивную функцию)

def funct(N):
    if N == 1:
        return True
    elif N % 2 == 0:
        return funct(N // 2)
    else:
        return False

N = int(input("Введите натуральное число: "))

if funct(N):
    print("YES")
else:
    print("NO")