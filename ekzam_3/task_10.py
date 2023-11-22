# 10) Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием
# (может быть несколько и брони может быть несколько. Так же может быть ничего)
# Выведите весь арсенал робота на экран

class Robot:
    def __init__(self, name, weapon=None, armor=None):
        self.name = name
        self.weapon = weapon
        self.armor = armor

class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

class Ammunition:
    def __init__(self, name, protection, durability):
        self.name = name
        self.protection = protection
        self.durability = durability

sword = Weapon("Меч", 10, 100)
gun = Weapon("Автомат", 20, 150)

# Создаем амуницию
armor = Ammunition("Броня", 50, 200)
helmet = Ammunition("Шлем", 30, 100)

# Создаем робота с выбранным оружием и амуницией
robot1 = Robot("Полицейский", weapon=gun, armor=armor)
robot2 = Robot("Рыцарь", weapon=sword, armor=helmet)

# Выводим весь арсенал робота на экран
print(f"Робот {robot1.name} вооружен {robot1.weapon.name} (урон: {robot1.weapon.damage}, "
      f"прочность: {robot1.weapon.durability}) и защищен {robot1.armor.name} (защита: {robot1.armor.protection}, "
      f"прочность: {robot1.armor.durability}).")
print(f"Робот {robot2.name} вооружен {robot2.weapon.name} (урон: {robot2.weapon.damage},"
      f" прочность: {robot2.weapon.durability}) и защищен {robot2.armor.name} (защита: {robot2.armor.protection}, "
      f"прочность: {robot2.armor.durability}).")
