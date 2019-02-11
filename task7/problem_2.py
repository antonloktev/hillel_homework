# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
import os
import json


class JsonControl(object):
    def __init__(self, file):
        self._file = file

    def append_data(self, data):
        with open(self._file, 'r') as f_r:
            new_file = json.load(f_r)
            new_file.update(data)
        with open(self._file, 'w') as f_w:
            json.dump(new_file, f_w, indent=4)

    def read_file(self):
        with open(self._file, 'r') as f:
            return json.load(f)

    @staticmethod
    def merge_files(new_file, *files):
        with open(new_file, 'w') as n_f:
            first = True
            for file in files:
                with open(file, 'r') as f:
                    if first:
                        n_f.write('[')
                        first = False
                    else:
                        n_f.write(',')
                    data = json.load(f)
                json.dump(data, n_f, indent=4)
            n_f.write(']')

    def get_relative_path(self):
        rel_path = os.path.relpath(self._file)
        return rel_path

    def get_absolute_path(self):
        abs_path = os.path.abspath(self._file)
        return abs_path


j = JsonControl('example.json')
print(j.read_file())
print(j.get_relative_path())
print(j.get_absolute_path())
dict = {'ex_key': 'ex_value', 'new_key': 42, 'a_list': [2, 12, 24, 42, 15]}
j.append_data(dict)
print(j.read_file())
more_data = {'kek': 'lol', '42': {'figure': 'circle'}}
j.append_data(more_data)
print(j.read_file())

js = JsonControl('new_file.json')
js.merge_files('new_file.json', 'example.json', 'example1.json')
print(js.read_file())
