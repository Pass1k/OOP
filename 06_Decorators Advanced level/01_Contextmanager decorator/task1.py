import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(ex)
    finally:
        end = time.time()
        print(end - start)


with timer() as t1:
    print('1 Part')
    val_1 = 100 * 100 * 1_000_000
    val_1 += 'abc'

with timer() as t2:
    print('1 Part')
    val_2 = 200 * 200 * 1_000_000

with timer() as t3:
    print('1 Part')
    val_3 = 900 * 900 * 1_000_000


