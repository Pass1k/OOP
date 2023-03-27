import logging
from datetime import datetime


def logging_dec(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        func_doc = func.__doc__

        print(f"Name of function: {func_name}")
        print(f"Documentation of function: {func_doc}")

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            with open('function_errors.log', 'a') as f:
                f.write(f"[{now}] Error in function {func_name}: {str(e)}\n")

    return wrapper


@logging_dec
def func():
    """It is a Documentation of function."""
    print("Function is working")
    raise ValueError("Error in function")


func()

