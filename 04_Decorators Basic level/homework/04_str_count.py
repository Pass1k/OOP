def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"The function {func.__name__} was ordered {wrapper.count} times")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def func1():
    print('Anakin Skywalker')


func1()
func1()
func1()
