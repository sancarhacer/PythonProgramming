import time
import tracemalloc
from functools import wraps


def performance(fn):
    """
    Decorator that measures performance statistics of a function.

    Each time the decorated function is called, this decorator updates
    three attributes:
        - performance.counter: number of total calls
        - performance.total_time: cumulative execution time in seconds
        - performance.total_mem: cumulative peak memory usage in bytes

    :param fn: Function to be decorated
    :return: Wrapped function with performance tracking
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that measures execution time and memory usage.

        :param args: Positional arguments passed to the function
        :param kwargs: Keyword arguments passed to the function
        :return: Result of the decorated function
        """
        performance.counter += 1

        tracemalloc.start()
        start_time = time.perf_counter()

        result = fn(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.total_time += (end_time - start_time)
        performance.total_mem += peak

        return result

    return wrapper


performance.counter = 0
performance.total_time = 0.0
performance.total_mem = 0
