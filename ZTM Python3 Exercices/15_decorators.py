from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"execution time: {execution_time} seconds")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 9


long_time()
