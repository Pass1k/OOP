import random

n = int(input('Введите число: '))

nums = [random.randint(-100, 100) for i in range(n)]

buffer_iter = iter(nums)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration as stop:
        print('Конец', stop)
        break