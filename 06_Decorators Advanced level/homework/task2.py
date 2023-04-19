def callback(route):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.route = route
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
