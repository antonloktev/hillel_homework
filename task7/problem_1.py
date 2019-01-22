# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)


class IP(object):
    def __init__(self, initial=None):
        if initial is None:
            initial = []
        self.value = initial

    def add_address(self, item):
        self.value.append(item)

    def clear_list(self):
        self.value.clear()

    def get_list(self):
        return self.value

    def get_reverse_items(self):
        res = []
        items = self.get_list()
        for item in items:
            s = str(item).split('.')
            s.reverse()
            rev_item = '.'.join(s)
            res.append(rev_item)
        return res

    def get_list_without_first_octets(self):
        res = []
        items = self.get_list()
        for item in items:
            s = str(item).split('.')
            s.pop(0)
            new_item = '.'.join(s)
            res.append(new_item)
        return res

    def get_list_of_last_octets(self):
        res = []
        items = self.get_list()
        for item in items:
            s = str(item).split('.')
            del s[0:3]
            new_item = ''.join(s)
            res.append(new_item)
        return res


ip = IP()
ip.add_address('10.11.12.13')
ip.add_address('192.0.2.1')
ip.add_address('172.16.254.1')
print('just a list of IPs:', ip.get_list())
print('IPs with reversed items:', ip.get_reverse_items())
print('IPs without first octets:', ip.get_list_without_first_octets())
print('only last octet of IPs:', ip.get_list_of_last_octets())

