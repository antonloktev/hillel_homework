# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен
class IngegerField:
    def __init__(self, number=None):
        self._number = number

    def __get__(self, instance, owner):
        return instance.__dict__['_number']

    def __set__(self, instance, value):
        instance.__dict__['_number'] = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10
assert data_row.number != new_data_row.number
