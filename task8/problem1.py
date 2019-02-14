# Задача-1
# Доделать задачу 2 которую вы получили на практике:
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять. Если флаг об исключении отсутствует,
# исключение должно быть поднято.
import os


class ChangeDir(object):
    def __init__(self, new_dir, exception=None):
        self._old_dir = os.getcwd()
        self._new_dir = new_dir
        self._exception = exception

    def __enter__(self):
        try:
            os.chdir(self._new_dir)
            print('Directory successfully changed')
        except Exception as exc:
            if type(exc).__name__ == self._exception.__name__:
                print(('{} successfully suppressed').format(self._exception.__name__))
            else:
                raise self._exception

    def __exit__(self, *args):
        os.chdir(self._old_dir)
        print('You\'re returned to the initial directory')


print(os.getcwd())
with ChangeDir('./new_dir', FileNotFoundError):
    print(os.getcwd())
    with open('output.file', 'w') as f:
        f.write('New line in new file in new directory, wow!')
print(os.getcwd())
