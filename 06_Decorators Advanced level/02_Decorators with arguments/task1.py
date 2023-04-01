def do_nice(n):
    def wrap_fun(func):
        """""декоратор do_twice, который дважды вызывает декорируемую функцию"""

        def wrapped_func(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return
        return wrapped_func
    return wrap_fun


@do_nice(5)
def greeting(name: str) -> None:
    print('Привет, {name}'.format(name=name))


greeting('Adam')
