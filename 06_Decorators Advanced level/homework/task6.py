from typing import Callable
import functools


def dec_with_args(dec_toenhance: Callable) -> Callable:
    def dec_maker(*args, **kwargs) -> Callable


def decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:

    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Here are the args and kwargs in decorator: ', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper


@decorator(100, 'RUB', 200, 'frieand')
def decorated_function(text: str, num: int) -> None:
    print("Helo", text, num)