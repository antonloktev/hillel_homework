# Задача-1
#
# Дан произвольный текст. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в тексте.
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы,
# то получим сообщение "HELLO".

text1 = "How are you? Eh, ok. Low or Lower? Ohhh."


def find_capital_letters(text):
    return "".join(c for c in text if c.isupper())


print(find_capital_letters(text1))

# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.

numbers = [341, 561, 645, 1105, 1387, 1729, 1905]


def multiply_with_even_indexes(num_list):
    sum_of_even_indexes = sum(x for x in num_list if num_list.index(x) % 2 == 0)
    return sum_of_even_indexes * num_list[-1]


print(multiply_with_even_indexes(numbers))

# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все


new_text = ". It's a text..."


def without_dots_comas(text):
    no_dots = text.replace(".", "")
    return no_dots.replace(",", "")


def find_word(text):
    words = without_dots_comas(text).split()
    result = []
    for i in range(len(words)):
        if words[i].isalpha() or words[i].count(chr(39)):
            result.append(words[i])
    return result[0] if len(result) else "There are no words :("


print(find_word(new_text))


# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.

text = "python"


def swap_first_last(string):
    list_of_letters = list(string)
    list_of_letters[0], list_of_letters[-1] = list_of_letters[-1], list_of_letters[0]
    return "".join(list_of_letters)


print(swap_first_last(text))


# def swap_first_last(string):


# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ("e", "x", "e", "r", "c", "i", "s", "e", "s") == 'exercises

tuple_of_letters = ("e", "x", "e", "r", "c", "i", "s", "e", "s")


def convert_to_string(tup):
    return "".join(tup)


print(convert_to_string(tuple_of_letters))
