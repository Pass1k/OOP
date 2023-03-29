class Figure:

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Reactangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

