
from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print('1-----')
print(fibonacci)
# <function fibonacci at 0x1046238b0>
print('2-----')
help(fibonacci)

import pickle
print(pickle.dumps(fibonacci))