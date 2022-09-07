class Spam:
    numInstances = 0 # Вместо статического метода используется метод класса
    def __init__(self):
        Spam.numInstances += 1
    def printNum(cls):
        print(f"Num is: {cls.numInstances}")
        #   Количество экземпляров
    printNum = classmethod(printNum)

a, b = Spam(), Spam()
a.printNum() # В первом аргументе передается класс
Spam.printNum() # Также в первом аргументе передается класс

class Sub(Spam):
    def printNum(cls):
        print("Extra stuff...", cls) # Переопределение метода класса
        Spam.printNum() # С вызовом первоначального метода
    printNum = classmethod(printNum)

class Other(Spam): # Наследование метода класса
    pass

x = Sub()
y = Spam()
x.printNum() # Вызов из экземпляра класса
Sub.printNum() # Вызов из самого подкласса
y.printNum() # Вызов из экземпляра суперкласса
z = Other()
z.printNum() # Вызов из более низкого подкласса
