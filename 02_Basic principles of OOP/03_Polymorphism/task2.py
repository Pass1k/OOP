class Can_Fly():
    def __init__(self, height = 0, speed = 0):
        self.height = height
        self.speed = speed

    def go_fly(self):
        pass

    def fly(self):
        pass

    def come_down(self):
        self.height = 0
        self.speed = 0

    def info(self):
        return f'Высота: {self.height}\nСкорость: {self.speed}'


class Butterfly(Can_Fly):
    def go_fly(self):
        return f'Взлететь (высота = {self.height})'

    def fly(self):
        return f'Лететь (скорость = {self.speed}).'

    def info(self):
        return f'Высота: {self.height}\nСкорость: {self.speed}'


class Rocket(Can_Fly):
    def go_fly(self):
        return f'Взлететь (высота = {self.height})'

    def fly(self):
        return f'Лететь (скорость = {self.speed}).'

    def come_down(self):
        return f'Приземлиться (высота = {self.height}, взрыв).'

    def boom(self):
        return f'Boom!'

geon = [
    Butterfly(1, 0.5),
    Rocket(500, 1000)
]

for i in geon:
    print(i.go_fly())
    print(i.fly())

print(geon[1].come_down())
print(geon[1].boom())