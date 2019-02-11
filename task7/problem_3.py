# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


class Switch(object):
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


s = Switch(1, '00:1B:44:11:3A:B7', '172.16.254.1', 'user', 'pass123')

print('Old data:')
print(s.unit_name)
print(s.mac_address)
print(s.ip_address)
print(s.login)
print(s.password)

s.unit_name = 42
s.mac_address = '00:1C:B3:09:85:15'
s.ip_address = '192.0.2.1'
s.login = 'master'
s.password = '_23$dfgnjUowei@!'

print('\nNew data:')
print(s.unit_name)
print(s.mac_address)
print(s.ip_address)
print(s.login)
print(s.password)
