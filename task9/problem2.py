# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


class AnotherClass():
    pass


class Singleton1(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)
        return cls._instances


class MyClass1(metaclass=Singleton1):
    pass


a = MyClass()
b = MyClass()
assert id(a) == id(b)

c = AnotherClass()
d = AnotherClass
assert id(c) != id(d)

e = MyClass1()
f = MyClass1()
assert id(e) == id(f)

