from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('The function {func} was ordered {count} times'.format(
            func=func.__name__, count=wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
def test():
    print('test')


test()

test()
test()