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
