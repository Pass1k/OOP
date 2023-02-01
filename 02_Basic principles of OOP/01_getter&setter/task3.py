class Point:
    def __init__(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def getter(self):
        return self.__x, self.__y

    def setter(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Хуй соси')




pt = Point(5, 10)
pt.setter(6, 87)

print(pt.getter())