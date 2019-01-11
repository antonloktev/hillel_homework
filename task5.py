# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались.
# Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных значений
# превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
#
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
#
# Задача-2
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
# а сколько раз значение было взято из кеша, сколько места свободно в кеше)
#
# Задача-3
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_clear - очищает кеш
#
# Пример обращения к служебному методу декоратора

#
# def decorator(my_func):
#      def wrapper():
#            my_func()
#
#      def cache_clear():
#            pass
#
#      wrapper.cache_clear = cache_clear
#      return wrapper
#
# @decorator
# def my_func():


# my_func.cache_clear()

from functools import wraps
from collections import OrderedDict


def lru_cache(maxsize=4):
    def decoration_function(user_function):
        cache = OrderedDict()
        cur_size = 0
        free_space = maxsize

        @wraps(user_function)
        def wrapper(*args, **kwargs):
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            if key in cache:
                result = cache.pop(key)
                wrapper.hits += 1
            else:
                result = user_function(*args, **kwargs)
                wrapper.misses += 1
                wrapper.cur_size += 1
                wrapper.free_space -= 1
                if len(cache) >= maxsize:
                    cache.popitem()
                    wrapper.cur_size = maxsize
                    wrapper.free_space = 0
            cache[key] = result
            return result

        def cache_info():
            print({'Cache': dict(cache)}),
            print('Info:\n hits: {}\t misses: {}\n current size of cache: {}\n free space: {}\n'
                  .format(wrapper.hits, wrapper.misses, wrapper.cur_size, wrapper.free_space))

        def cache_clear():
            cache.clear()
            wrapper.hits = wrapper.misses = wrapper.cur_size = 0
            wrapper.free_space = maxsize
            print('\nCache has been cleared!\n')

        wrapper.hits = wrapper.misses = 0
        wrapper.cur_size = cur_size
        wrapper.free_space = free_space
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decoration_function


@lru_cache()
def func(a, b):
    return a**b + b**a


if __name__ == '__main__':
    func.cache_info()
    func(1, 3)
    func(3, 1)
    func(1, 3)
    func.cache_info()
    func(1, 4)
    func.cache_info()
    func(1, 45)
    func(2, 12)
    func.cache_info()
    func.cache_clear()
    func.cache_info()
    func(2, 4)
    func(2, 5)
    func(1, 2)
    func(1, 16)
    func(1, 20)
    func.cache_info()
