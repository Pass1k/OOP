import time


def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@delay(1)
def func1():
    print('Задержка в 1 секунду.')


@delay(2)
def func2():
    print('Задержка в 2 секунды.')


@delay(3)
def func3():
    print('Задержка в 3 секунды.')


func1()
func2()
func3()
