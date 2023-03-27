def how_are_you(func):
    def wrapper():
        answer = input('Как ваши дела? ')
        print('А у меня не очень! Ладно, вот ваша функиця')
        func()

    return wrapper


@how_are_you
def test1():
    print('Что-то тут присходит')


@how_are_you
def test2():
    print('Вот так вот работает декоратор')


test1()
test2()
