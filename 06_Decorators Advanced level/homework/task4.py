from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable[..., Callable]) -> Callable[..., Callable]:
    def new_decorator(*args, **kwargs) -> Callable[..., Callable]:
        def wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return wrapper
    return new_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    print("Переданные арги и кварги в декоратор:", args, kwargs)
    
    def wrapper(*func_args, **func_kwargs):
        func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
