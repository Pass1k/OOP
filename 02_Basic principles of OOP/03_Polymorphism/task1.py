class Unit:
    def get_hit(self):
        raise NotImplementedError('В дочерных классах нужно преопределить метод "get_hit"')


class Solder(Unit):
    def __init__(self, hitpoint = 100):
        self.damage = None
        self.hitpoint = hitpoint

    def get_hit(self, damage = 10):
        self.damage = damage
        return f'Количество жизни {self.hitpoint - self.damage}'


class Citizen(Unit):
    def __init__(self, hitpoint = 100):
        self.hitpoint = hitpoint

    def get_hit(self, damage = 10):
        self.damage = damage
        return f'Количество жизни {self.hitpoint - self.damage}'


geom = [
    Solder(110), Solder(150),
    Citizen(80), Citizen(65)
]

for i in geom:
    print(i.get_hit())





