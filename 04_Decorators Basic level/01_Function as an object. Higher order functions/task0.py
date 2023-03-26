import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    started_time = time.time()
    result = func()
    ended_time = time.time()
    run_time = run_time = round(ended_time - started_time, 4)
    print('Time work: {}'.format(run_time))

    return result


def squares_sum() -> int:
    number = 109
    result = 0
    for i in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])

    return result


my_result = timer(squares_sum)
print(my_result)