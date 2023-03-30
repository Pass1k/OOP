class Example:

    def __init__(self):
        print('order of __init__')

    def __enter__(self):
        print('Order of __enter__')
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Order of __exit__')
        if exc_type:
            print(f'Тип ошибки: {exc_type} \nЗначение ошибки: {exc_val} \nСдедд.Ошибки: {exc_tb}')
            return True


my_onj = Example()

with my_onj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_onj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь')