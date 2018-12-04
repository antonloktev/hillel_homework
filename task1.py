import random
import copy


# problem 1
def generate_dict():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dictionary = {key: key * key for key in keys}
    print(dictionary)


# problem 2
def get_even_list():
    start = 0
    finish = 100
    array = list(range(start, finish + 1))
    even_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array.append(i)
    print(even_array)


# problem 3
def replace_cons(text):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vovels = ['a', 'e', 'i', 'o', 'u', 'y']
    for character in text:
        if character.lower() in consonants:
            text = text.replace(character, random.choice(vovels))
    print(string)


# problem 4.1
def get_set(x):
    unique_element = set(x)
    print(list(unique_element))


# problem 4.2
def get_maximums(x):
    maximums = []
    tmp = copy.deepcopy(x)
    for i in range(3):
        maximum = max(tmp)
        maximums.append(maximum)
        tmp.remove(maximum)
    print(maximums)


# problem 4.3
def get_index_of_min(x):
    minimum = min(x)
    index = x.index(minimum)
    print(index)


# problem 4.4
def reverse_list(x):
    x.reverse()
    print(x)


# problem 5
def get_same_keys(x, y):
    print(x.keys() & y.keys())


numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
string = 'To be or not to be. That is the question number 42. ' \
         'This word will consist only of vowels: bcdsrtvwxz.'
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}


generate_dict()

get_even_list()

replace_cons(string)

get_set(numbers)
get_maximums(numbers)
get_index_of_min(numbers)
reverse_list(numbers)

get_same_keys(dict_one, dict_two)
