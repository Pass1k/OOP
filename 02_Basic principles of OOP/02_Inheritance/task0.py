class Robot:
    def __init__(self, model):
        self.__model = model


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        return f'Я защищаю эту суку с ганом {self.__gun}'

class Cleaner(Robot):
    def __init__(self, model, trash=0):
        super().__init__(model)
        self.__trash = trash

    def operate(self):
        print(f'До очистки {self.__trash}')
        self.__trash = 0
        return f'он пылесосит пол {self.__trash}'

wr = WarRobot(12, 'AWP')
cl = Cleaner(13, 12)

print(wr.operate())
print(cl.operate())
