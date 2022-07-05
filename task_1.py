import re
from functools import wraps
import time


# Декоратор для вычисления времени выполнения
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = round((end_time - start_time) * 1000)
        print(f'Function {func.__name__} return {result} and took {total_time:.2f} ms')
        return result

    return timeit_wrapper


def is_valid(user_str):
    # Проверка формы данных
    pat = re.compile(r'1+0+')
    if re.fullmatch(pat, user_str) is None:
        raise ValueError("Bad data format")
    return True


@timeit
def method_1(user_str):
    # Используем встроенную функцию
    try:
        index = user_str.index('0')
        return index
    except ValueError:
        return -1


@timeit
def method_2(user_str):
    # Brutal force
    index = 0
    for i in user_str:
        if i == '0':
            return index
        index += 1


@timeit
def method_3(user_str):
    # Бинарный поиск
    left = -1
    right = len(user_str)
    while right - left > 1:
        middle = (left + right) // 2
        if user_str[middle] == '0':
            right = middle
        else:
            left = middle
    return right


@timeit
def method_4(user_str):
    # Используем regex
    return re.search("0", user_str).start()


if __name__ == "__main__":

    METHODS = (method_1, method_2, method_3, method_4)
    test_data = '1' * 100000000 + '0' * 100000000

    try:
        if is_valid(test_data):
            for method in METHODS:
                method(test_data)
    except ValueError as ve:
        print(ve)
