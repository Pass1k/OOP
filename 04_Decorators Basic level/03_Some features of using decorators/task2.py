plugins = {}


def go_to_plugins(func):
    plugins[func.__name__] = func
    return func


@go_to_plugins
def hello():
    print('Hello!')


print(plugins)