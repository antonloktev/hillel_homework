# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инструкций
import time


class Timer(object):
    def __init__(self, name='Some block'):
        self._name = name

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args):
        self._end = time.time()
        self._execution_time = self._end - self._start
        print(('Execution time for {} is: {}').format(self._name, self._execution_time))


with Timer('Loop'):
    for i, k in enumerate(range(501)):
        print(i, k ** k)


@contextmanager
def timer(name='Some block'):
    start = time.time()
    try:
        yield
    except Exception as exc:
        print(('There is an exception: {}').format(type(exc).__name__))
    finally:
        end = time.time()
        execution_time = end - start
        print(('Execution time for {} is: {}').format(name, execution_time))


with timer('Just the same loop'):
    for i, k in enumerate(range(501)):
        print(i, k ** k)

