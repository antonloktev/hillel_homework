# Задача -2
# Описать задачу выше но уже с использованием @contexmanager
import os
from contextlib import contextmanager


@contextmanager
def change_dir(new_dir, exception):
    old_dir = os.getcwd()
    try:
        yield os.chdir(new_dir)
        print('Directory successfully changed')
    except Exception as exc:
        if type(exc).__name__ == exception.__name__:
            print(('{} successfully suppressed').format(exception.__name__))
            yield
        else:
            raise exception
    finally:
        os.chdir(old_dir)
        print('You\'re returned to the initial directory')


print(os.getcwd())
with change_dir('./new_dir1', FileNotFoundError):
    print(os.getcwd())
    with open('output.file', 'w') as f:
        f.write('New line in new file in new directory, wow!')
print(os.getcwd())

