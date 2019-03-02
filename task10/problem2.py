import time
from functools import wraps


def coroutine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.__next__()
        return gen
    return wrapper


def follow(f_file, target):
    f_file.seek(0, 2)
    while True:
        line = f_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def dispenser(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


with open("log.txt") as f:
    p = printer()
    follow(f,
           dispenser([
               grep('python', p),
               grep('is', p),
               grep('great', p)
           ])
           )
