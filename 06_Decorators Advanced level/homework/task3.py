from datetime import datetime
import time


def log_methods(date_format):
    def decorator(cls):
        class DecoratedClass(cls):
            def __getattribute__(self, name):
                attr = super().__getattribute__(name)
                if callable(attr) and not name.startswith("__"):
                    def wrapper(*args, **kwargs):
                        start_time = time.time()
                        date_time = datetime.now().strftime(date_format)
                        print(f"Запускается '{type(self).__name__}.{name}'. Дата и время запуска: {date_time}.")
                        result = attr(*args, **kwargs)
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print(f"Завершение '{type(self).__name__}.{name}', время работы = {elapsed_time:.3f} s.")
                        return result
                    return wrapper
                return attr
        return DecoratedClass
    return decorator


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
