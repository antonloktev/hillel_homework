# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.
# Например ваша функция может иметь вид
# def my_func():
#     raise ValueError("some text error")

# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента


def selected_surnames(read, write):
    with open(read, "r") as fr, open(write, "w") as fw:
        for line in fr:
            last_name = line.split(" ", 1)[1]
            if last_name[0] in ("C", "K"):
                fw.write(line)


selected_surnames("task6/phone_numbers.txt", "task6/phone_ck.txt")
