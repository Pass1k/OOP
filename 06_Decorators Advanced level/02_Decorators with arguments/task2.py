from time import sleep


def slow_it_now(_func=None, *, n=1):
    def slowdown_ns(func):
        def wrapper(*args, **kwargs):
            sleep(n)
            result = func(*args, **kwargs)
            return result
        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now
def test() -> None:
    """Проверка декоратора и вывод прстого сообщения return:"""
    print('Here`s happening somthing')


test()