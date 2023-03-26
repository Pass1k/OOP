from typing import Callable, Any


def func_1(x):
    return x + 10


def func_2(func, number):
    return func(number) * func(number)


print(func_2(func_1, 9))