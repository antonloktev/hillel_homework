# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re


class EmailDescriptor:
    def __init__(self, email=None):
        self._email = email

    def __get__(self, instance, owner):
        return self._email

    def __set__(self, instance, value):
        if re.match(r'^[\w.-]+@\w+\.+\w', value) is not None:
            self._email = value
        else:
            raise ValueError('Your e-mail is not valid')


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"
my_class.email = "novalidemail"


