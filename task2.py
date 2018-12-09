from operator import itemgetter
import itertools

#1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}
]

#1.1) отсортировать массив из словарей по значению ключа ‘age' 


def sort_by_key(dictionary, key):
    sorted_data = sorted(dictionary, key=itemgetter(key))
    return sorted_data

#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :

result = {
   'Kiev': [{'name': 'Viktor', 'age': 30 },
            {'name': 'Andrey', 'age': 34}],
   'Dnepr': [ {'name': 'Maksim', 'age': 20 },
              {'name': 'Artem', 'age': 50}],
   'Lviv': [ {'name': 'Vladimir', 'age': 32 },
             {'name': 'Dmitriy', 'age': 21}]
}


def group_by_key(data):
    sorted_data = sorted(data, key=itemgetter('city'))
    for key, group in itertools.groupby(sorted_data, key=lambda x: x['city']):
        print("'%s':" % key),
        print(list(group))


# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:


def most_frequent(list):
    result = max(list, key=list.count)
    return result

# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.


def multiplication_of_digits(number):
    number_list = [int(n) for n in str(number)]
    result = 1
    for number in number_list:
        if number != 0:
            result *= number
        else:
            continue
    return result

# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


def exponentiation_by_index(list, number):
    res = -1
    if number < len(list):
        res = list[number] ** number
    return res

# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.


def three_words(text):
    result = False
    words = text.split()
    for i in range(1, len(words)-1):
        if words[i].isalpha() and words[i-1].isalpha() and words[i+1].isalpha():
            result = True
    return result


# print(sort_by_key(data, 'age'))

# group_by_key(data)

list_var = ['a', 'a', 'bi', 'bi', 'bi']
# print(most_frequent(list_var))


x = 123405
# print(multiplication_of_digits(x))


nums = [1, 2, 3, 4, 5]
n = 3
# print(exponentiation_by_index(nums, n))

string = 'hello 1 one two three 15 world is mine'
# print(three_words(string))


