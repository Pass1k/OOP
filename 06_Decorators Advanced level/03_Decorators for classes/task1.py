import datetime

def logged(func):
    def wrapped(*args, **kwargs):
        print('Lunched in: ', datetime.datetime.now())
        return func(*args, **kwargs)
    return wrapped


def decorator(cls):
    for i in dir(cls):
        if i.startswith('__'):
            continue
        a = getattr(cls, i)
        if hasattr(a, '__call__'):
            decorator_a = logged(a)
            setattr(cls, i, decorator_a)

    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Here`s method')
        number = 100
        result = 0
        for i in range(number + 1):
            result += sum([i ** 2 for i in range(1000)])

        return result

A().test_sum_1()