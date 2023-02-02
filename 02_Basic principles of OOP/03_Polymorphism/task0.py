class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочерных классах нужно преопределить метод "get_pr"')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


geom = [
    Rectangle(1, 2), Rectangle(3, 4),
    Square(3), Square(10),
    Triangle(2, 4, 6), Triangle(3, 6, 9)
]

for i in geom:
    print(i.get_pr())