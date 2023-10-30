# 1. Создайте суперкласс «Персональные компьютеры» и на его основе подклассы:
# «Настольные ПК» и «Ноутбуки». В классе-родителе определите общие свойства:
# размер памяти, модель. А в классах-потомках уникальные свойства:- для настольных:
# монитор, клавиатура, мышь; и метод для вывода этой информации
# - для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации.
class PC:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

    def get_info(self):
        print("Модель:", self.model)
        print("Количество памяти:", self.memory)

class Desktop_PC(PC):
    def __init__(self, memory ,model, monitor, keyboard, mouse):
        super().__init__(memory ,model)
        self.monitor = monitor
        self.keyboard = keyboard
        self. mouse = mouse
    def info_desktop(self):
        print(f"Модель {self.model}, память {self.memory}, монитор {self.monitor}, клавиатура {self.keyboard}, мышь {self.mouse}")

class Notebook(PC):
    def __init__(self, memory ,model, dimensions,diagonal):
        super().__init__(memory, model)
        self.dimensions = dimensions
        self. diagonal = diagonal
    def info_notebook(self):
        print(f"Модель {self.model}, память {self.memory}, размеры {self.dimensions}, диагональ экрана {self.diagonal}")

pc2 = Desktop_PC(8,'Dell','samsung','logitec','net')
pc2.get_info()
pc2.info_desktop()
pc3 = Notebook(16,'Asus', "259x378x25.3",15.6)
pc3.get_info()
pc3.info_notebook()