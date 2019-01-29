# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.
import re


def diff(first, second):
    """ This function finds the difference between two list with keeping order."""
    second = set(second)
    return [item for item in first if item not in second]


def delete_words_by_length(file, low_b=3, up_b=5):
    """ This function deletes words in the text by given length and overwrites the file.
    Hereinafter, the word 'puncs' will mean punctuation marks in the text.
    Speciality: function deletes an even number of words on each line.
    For the odd case it will overwrite the last word in a line.
    :param file: File which needs to be changed and overwritten.
    :param low_b: Lower bound of word's length you want to delete.
    :param up_b: Upper bound... (the same)
    """
    with open(file, "r+") as f:
        new_text = ""
        for line in f:
            words = re.findall(r"[\w']+|[.,!?;:]", line)  # get a list of word including puncs as individual items
            short_words = [word for word in words if low_b <= len(word) <= up_b]
            if len(short_words) % 2 == 1:
                del short_words[-1:]
            difference = diff(words, short_words)
            new_line = " ".join(difference)
            corr_spaces = re.sub(r"\s([.,!?;:](?:\s|$))", r"\1", new_line)  # getting correct spaces before puncs
            new_text = "{}{}\n".format(new_text, corr_spaces)
        f.seek(0)
        f.truncate()
        f.write(new_text)


delete_words_by_length("delete3-5.txt")

# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def selected_surnames(read, write):
    """ This function writes in output file first name, last name and prone number of persons from a general list of
    people (input file).
    :param read: Input file containing first name, last names and phone number of person
    :param write: Output file containing same info about people whose last name begins with a letter C or K
    """
    with open(read, "r") as fr, open(write, "w") as fw:
        for line in fr:
            last_name = line.split(" ", 1)[1]
            if last_name[0] in ("C", "K"):
                fw.write(line)


selected_surnames("phone_numbers.txt", "phone_ck.txt")

