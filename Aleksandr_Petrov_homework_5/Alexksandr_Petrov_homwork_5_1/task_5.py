# 5. Сколько можно купить быков, коров и телят, если плата за быка 10 рублей,
# за корову — 5 рублей, за теленка — полтинник (0.5 рубля),
# если на 100 рублей надо купить 100 голов скота.
bulls = 0
cows = 0
calves = 0
for i in range(0, 101):
  for j in range(0, 101):
    for k in range(0, 101):
      if 10*i + 5*j + 0.5*k == 100 and i + j + k == 100:
        bulls = i
        cows = j
        calves = k
        break
print(f"Можно купить {bulls} быков, {cows} коров и {calves} телят.")