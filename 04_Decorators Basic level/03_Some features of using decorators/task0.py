from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return "Hello {name}".format(name=name)


@register
def say_goodbye(name: str) -> str:
    return "GoodBye {name}".format(name=name)


print(PLUGINS)
print(say_hello('Parasat'))
print(say_goodbye('Parasat'))