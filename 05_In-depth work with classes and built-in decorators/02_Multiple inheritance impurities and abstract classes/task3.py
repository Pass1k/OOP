from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, pos_x, pos_y, lenght, width):
        self.pos_x = pos_y
        self.pos_y = pos_y
        self.lenght = lenght
        self.widht = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, width, length):
        pass


class Square(Figure):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)

    def resize(self, width, length):
        if width == length:
            self.widht = width
            self.lenght = length
        else:
            print('У квадрата стороны равны!')