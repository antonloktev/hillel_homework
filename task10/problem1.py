# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем
import os


def get_unique_lines(inp_file):
    unique_lines = set()
    if not os.path.exists(inp_file):
        raise FileNotFoundError('Could not find file')
    with open(inp_file) as f:
        for line in f:
            if line.strip() not in unique_lines:
                unique_lines.add(line.strip())
                yield line


for line in get_unique_lines('text_file.txt'):
    print(line)

