# Класс-итератор:
class MyIter:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


my_iter = MyIter(int(input('Введите число: ')))
for i in my_iter:
    print(i)


# Функция-генератор:
def generator(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


my_generator = generator((int(input('Введите число: '))))
for i in my_generator:
    print(i)


# Генераторное выражение:
n = int(input('Введите число: '))
squares = (i ** 2 for i in range(1, n + 1))
for square in squares:
    print(square)


