import time


def timer(func):
    start = time.time()
    func()
    end = time.time()
    return end - start


def hard_func():
    return [x ** 2 ** x for x in range(22)]


print(timer(hard_func))



