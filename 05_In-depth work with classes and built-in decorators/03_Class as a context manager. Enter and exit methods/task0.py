import time


class Timer:
    def __init__(self) -> None:
        print('Work time')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time()-self.start)
        if exc_type is TypeError:
            return True


with Timer() as t1:
    print('First part')
    val_1 = 100 * 100 ** 1_000_000

with Timer() as t2:
    print('First part')
    val_2 = 200 * 200 ** 1_000_000

with Timer() as t3:
    print('First part')
    val_3 = 300 * 300 ** 1_000_000







