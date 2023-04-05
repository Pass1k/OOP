import datetime


def decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)

        print('Created time -', datetime.datetime.now())
        print('Method:', end=' ')
        for i in dir(cls):
            if i.startswith('__'):
                continue
            print(i, end=' ')
        print()
        return instance
    return wrapper


@decorator
class Example:

    def hello(self):
        print('Hi')
        
    def hello_2(self):
        print('Hello')


Example()
Example()