# Задача №1
# Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов,
# пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
# def split_pairs(a):
#     b = []
#     for i in range(0, len(a), 2):
#         para = a[i:i + 2]
#         if len(para) == 1:
#             b.append(para + '_')
#         else:
#             b.append(para)
#     return b
    # return [a[i:i + 2] + '_' if len(a[i:i + 2]) == 1 else a[i:i + 2] for i in range(0, len(a), 2)]
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(split_pairs('abcd')))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(split_pairs('abcd')) == ['ab', 'cd']
#     assert list(split_pairs('abc')) == ['ab', 'c_']
#     assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
#     assert list(split_pairs('a')) == ['a_']
#     assert list(split_pairs('')) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Решение другого пользователя
# def split_pairs(a):
#     return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]
# a = 'abcdf'
# print(a[::2])
# print(a[1::2])
# print(*zip(a[::2],a[1::2]))
# # b = []
# # for i in zip(a[::2],a[1::2]):
# #     b.extend(i)
# # print(b)
# for ch1,ch2 in zip(a[::2],a[1::2]):
#     print(ch1+ch2)

# Задача №2
# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд .
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# def checkio(words: str) -> bool:
#     b = winner = 0
#     for i in words.split():
#         if i.isdigit():
#             b = 0
#         else:
#             b += 1
#             winner = max(winner, b)
#     return True if winner > 2 else False
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio("Hello World hello"))
#
#     assert checkio("Hello World hello") == True, "Hello"
#     assert checkio("He is 123 man") == False, "123 man"
#     assert checkio("1 2 3 4") == False, "Digits"
#     assert checkio("bla bla bla bla") == True, "Bla Bla"
#     assert checkio("Hi") == False, "Hi"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# Решение другого пользователя

# def checkio(words):
#     succ = 0
#     for word in words.split():
#         succ = (succ + 1)*word.isalpha()
#         if succ == 3: return True
#     else: return False

# Задача №3
# Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
# Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано
# в первом аргументе, а сами данные по товарам будут переданы вторым аргументом.

# def bigger_price(limit: int, data: list) -> list:
#     return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
#
#
# if __name__ == '__main__':
#     from pprint import pprint
#     print('Example:')
#     pprint(bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]))
#
#     # These "asserts" using for self-checking and not for auto-testing
#     assert bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]) == [
#         {"name": "wine", "price": 138},
#         {"name": "bread", "price": 100}
#     ], "First"
#
#     assert bigger_price(1, [
#         {"name": "pen", "price": 5},
#         {"name": "whiteboard", "price": 170}
#     ]) == [{"name": "whiteboard", "price": 170}], "Second"
#
#     print('Done! Looks like it is fine. Go and check it')

# Задача №4
# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими
# маркерами. Но есть несколько важных условий:
# Начальный и конечный маркеры всегда разные
# Если нет начального маркера, то началом считать начало строки
# Если нет конечного маркера, то концом считать конец строки
# Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
# Если конечный маркер стоит перед начальным, то вернуть пустую строку

# def between_markers(text: str, begin: str, end: str) -> str:
#     # if begin in text and end in text:
#     #     return text[text.index(begin) + len(begin):text.index(end)]
#     # elif begin not in text and end in text:
#     #     return text[:text.index(end)]
#     # elif begin in text and end not in text:
#     #     return text[text.index(begin) + len(begin):]
#     # else:
#     #     return text
#     b = text.index(begin) + len(begin) if begin in text else None
#     c = text.index(end) if end in text else None
#
#     return text[b:c]
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
#     assert between_markers("<head><title>My new site</title></head>",
#                            "<title>", "</title>") == "My new site", "HTML"
#     assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
#     assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
#     assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
#     assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
#     print('Wow, you are doing pretty good. Time to check it!')


# Решение другого пользователя
# def between_markers(text: str, begin: str, end: str) -> str:
#     start = text.find(begin) + len(begin) if begin in text else None
#     stop = text.find(end) if end in text else None
#     return text[start:stop]

# Задача №5
# Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления,
# то есть по количеству раз, которое они появляются в элементах. Если два элемента имеют одинаковую частоту,
# они должны оказаться в том же порядке, в котором стояли изначально в итераторе.

# def frequency_sort(items):
#     # your code here
#     # b = []
#     # c = []
#     # for i in items:
#     #     if not i in b:
#     #         b.append(i)
#     # for j in b:
#     #     c.extend([j] * items.count(j))
#     #
#     # return sorted(c, key=c.count, reverse=True)

#     короткое верное решение
#     return sorted(sorted(items, key=items.index), key=items.count, reverse=True)
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [[4, 4, 4, 4, 6, 6, 2, 2]1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# items = [4, 4, 4, 4, 6, 6, 2, 2]
#
# # print(sorted(sorted(a, key=a.index), key=a.count, reverse=True))
# # print(sorted(a, key=a.count))
# # print(sorted(a, key=a.index))
# print(sorted(items, key=lambda x: (-items.count(x), items.index(x))))
# print(sorted(items, key=-items.count))

# Решение другого пользователя

# def frequency_sort(items):
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

########################################################################
###############################################################
#######################################################################
# Ваше задание - пересортировать список, расположив числа в порядке уменьшения их количества в списке.
# Если несколько чисел встречаются одинаково часто - их необходимо расположить в порядке от меньшего к большему,
# вне зависимости от того, в каком порядке они встречаются в исходном списке.
# Например: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
# frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]
# a = [5, 3, 8, 11, 5, 6, 6, 5]
#
# print(sorted(a, key=a.count))

# from typing import List
#
#
# def frequency_sorting(numbers: List[int]) -> List[int]:
#     # replace this for solution
#     return numbers
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(frequency_sorting([1, 2, 3, 4, 5]))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
#     assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
#         4,
#         4,
#         4,
#         3,
#         3,
#         11,
#         11,
#         7,
#         13,
#     ], "Not sorted"
#     assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
#         10,
#         10,
#         21,
#         21,
#         55,
#         55,
#         99,
#         99,
#     ], "Reversed"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# numbers = [3, 4, 11, 13, 11, 4, 4, 7, 3]
# print(sorted(sorted(numbers), key=numbers.count, reverse=True))

# #####################################################
##################################################################
# from typing import List
#
#
# def frequency_sorting(numbers: List[int]) -> List[int]:
#     # replace this for solution
#     # b = []
#     # c = []
#     # for i in sorted(numbers):
#     #     if not i in b:
#     #         b.append(i)
#     # for j in b:
#     #     c.extend([j] * numbers.count(j))
#     return sorted(sorted(numbers), key=numbers.count, reverse=True)
#
# if __name__ == "__main__":
#     print("Example:")
#     print(frequency_sorting([1, 2, 3, 4, 5]))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
#     assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
#         4,
#         4,
#         4,
#         3,
#         3,
#         11,
#         11,
#         7,
#         13,
#     ], "Not sorted"
#     assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
#         10,
#         10,
#         21,
#         21,
#         55,
#         55,
#         99,
#         99,
#     ], "Reversed"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# items = [5, 3, 0, 0, 4, 1, 4, 0, 7]
# b = filter(lambda i: i, sorted(items))
# print([next(b) if i else 0 for i in items]) # next работает только с итератором

#################################################################
######################################################################3

# Задача №6
# В этой миссии Вам надо определить, все ли элементы массива равны.
# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     # your code here
#     return all(elements[ind] == elements[ind + 1] for ind, i in enumerate(elements[:-1]))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([1, 2, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# a = [1, 2, 1]
# print(a[1:])
# print(a[:-1])

# Решение другого пользователя
# def all_the_same(elements):
#     return elements[1:] == elements[:-1]


# Задача №7
# Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
# Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
# Обратите внимание, что слова "hour" и "minute" (в единственном числе) используются только когда время 01:mm
# (1 hour) или hh:01 (1 minute).
# Во всех остальных случаях следует использовать "hours" и "minutes".

# from datetime import datetime
# def date_time(time: str) -> str:
#     time = datetime.strptime(time, '%d.%m.%Y %H:%M')
#     hour = 'hour' if time.hour == 1 else 'hours'
#     minute ='minute' if time.minute == 1 else 'minutes'
#
#     return time.strftime(f'%#d %B %Y year %#H {hour} %#M {minute}')
    # a = 's'
    # b = 's'
    # if c[3] == '1' and c[4] != '1':
    #     a = ''
    # elif c[4] == '1' and c[3] != '1':
    #     b = ''
    # elif c[3] and c[4] == '1':
    #     a = ''
    #     b = ''
    # return f'{c[0]} {c[1]} {c[2]} year {c[3]} hour{a} {c[4]} minute{b}'


# if __name__ == "__main__":
#     print("Example:")
#     print(date_time("01.01.2000 00:00"))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert (
#         date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
#     ), "Millenium"
#     assert (
#         date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
#     ), "Victory"
#     assert (
#         date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
#     ), "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Решение другого пользователя
# from datetime import datetime
#
# def checkio(time):
#     dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
#     hour = 'hour' if dt.hour == 1 else 'hours'
#     minute = 'minute' if dt.minute == 1 else 'minutes'
#     return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')

# Задача № 8
# Вам предоставляется набор координат, в которых расставлены белые пешки.
# Вы должны подсчитать количество защищенных пешек.

# def safe_pawns(pawns: set) -> int:
#     pawns_index = set()
#     for p in pawns:
#         row = int(p[1]) - 1
#         col = ord(p[0]) - 97
#         pawns_index.add((row, col))
#     count = 0
#     for row, col in pawns_index:
#         is_safe = ((row - 1, col - 1) in pawns_index) or ((row - 1, col + 1) in pawns_index)
#         if is_safe:
#             count += 1
#     return count

#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# a = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
# c, r = map(ord, a)
# print(c, r)

# Задача №8
# У вас есть список. Каждое значение из этого списка может быть либо строкой, либо целым числом.
# Ваша задача здесь — вернуть два значения. Первый — это конкатенация всех строк из заданного списка.
# Второй представляет собой сумму всех целых чисел из заданного списка.

# from typing import Tuple
#
#
# def sum_by_types(items: list) -> Tuple[str, int]:
#     b = ''
#     c = 0
#     d = []
#     for i in items:
#         if type(i) == str:
#             b += i
#         else:
#             c += i
#     d.append(b)
#     d.append(c)
#     return tuple(d)
# # print(tuple(filter(lambda x: isinstance(x, str), a)))
# #print(tuple(filter(lambda x: type(x) == int, a)))
#
# if __name__ == "__main__":
#     print("Example:")
#     print(sum_by_types([]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_by_types([]) == ("", 0)
#     assert sum_by_types([1, 2, 3]) == ("", 6)
#     assert sum_by_types(["1", 2, 3]) == ("1", 5)
#     assert sum_by_types(["1", "2", 3]) == ("12", 3)
#     assert sum_by_types(["1", "2", "3"]) == ("123", 0)
#     assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Решение другого пользователя

# def sum_by_types(items):
#     result = ['', 0]
#     for item in items:
#         result[isinstance(item, int)] += item
#     return result

# a = [1, 2, 3]
# b = ['', 0]
# for i in a:
#     b[isinstance(i, int)] += i
# print(b)
#     print(isinstance(i, str))

# Задача №9
# У вас есть список. Каждое значение из этого списка может быть либо строкой, либо целым числом.
# Ваша задача здесь — вернуть два значения. Первый — это конкатенация всех строк из заданного списка.
# Второй представляет собой сумму всех целых чисел из заданного списка.

# from typing import Tuple
#
#
# def follow(instructions: str) -> Tuple[int, int]:
#     b = [0, 0]
#     for i in instructions:
#         if i == 'f':
#             b[1] += 1
#         elif i == 'b':
#             b[1] -= 1
#         elif i == 'l':
#             b[0] -= 1
#         else:
#             b[0] += 1
#     return tuple(b)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(follow("fflff"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert follow("fflff") == (-1, 4)
#     assert follow("ffrff") == (1, 4)
#     assert follow("fblr") == (0, 0)
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# # Решение другого пользователя
# def follow(instructions):
#     c = instructions.count
#     return c('r') - c('l'), c('f') - c('b')


# Задача №10
# Для этого задания, вы будете использовать латинский алфавит (A-Z). У вас есть текст с латинскими буквами
# и знаками препинания. Вы должны проверить является ли предложение панграммой или нет. Регистр не имеет значения.

# def check_pangram(text):
#     '''
#         is the given text is a pangram.
#     '''
#     # your code here
#     a = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
#     return all(True if i in text.lower() else False for i in a)
#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
#     assert not check_pangram("ABCDEF"), "ABC"
#     assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
#     print('If it is done - it is Done. Go Check is NOW!')

# Решение другого пользователя
# from string import ascii_lowercase
#
#
# def check_pangram(text):
#     return set(ascii_lowercase).issubset(set(text.lower()))

# Задача №11
# Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата,
# принятого в Python (my_function_name) в CamelCase, принятый в JavaScript (MyFunctionName),
# где первая буква каждого слова - большая/заглавная.

# def to_camel_case(name: str) -> str:
#     #replace this for solution
#     return ''.join(i.title() for i in name.split('_'))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(to_camel_case('name'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert to_camel_case("my_function_name") == "MyFunctionName"
#     assert to_camel_case("i_phone") == "IPhone"
#     assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
#     assert to_camel_case("name") == "Name"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Решение другого пользователя
# def to_camel_case(name):
#     return name.title().replace('_', '')

# a = "my_function_name"
# print(a.title())

# Задача №12
# Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
# def find_message(message: str) -> str:
#     # your code here
#     return ''.join(i for i in message if i.isalpha() and i == i.upper())
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(find_message(('How are you? Eh, ok. Low or Lower? '
#  + 'Ohhh.')))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert find_message(('How are you? Eh, ok. Low or Lower? '
#  + 'Ohhh.')) == 'HELLO'
#     assert find_message('hello world!') == ''

#     assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# Решение другого пользователя

# find_message=lambda t:"".join(c for c in t if c.isupper())

# Задача №13
# YAML - это текст, а вам надо преобразовать его в объект. Но я не прошу вас реализовывать весь стандарт YAML,
# мы будем реализовывать его шаг за шагом.
# Первый шаг - это преобразование ключ-значение. Ключом может быть любая строка, из латинских букв и цифр.
# Значением может быть однострочная строка (которая состоит из пробелов, латинских букв и цифр) или число (int).
# def yaml(a):
#     b = {}
#     for i in a.split('\n'):
#         if i:
#             c, d = i.split(': ')
#             b[c] = int(d) if d.isdigit() else d
#     return b
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(yaml("""name: Alex
# age: 12"""))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert yaml("""name: Alex
# age: 12""") == {'age': 12, 'name': 'Alex'}
#     assert yaml("""name: Alex Fox
# age: 12
#
# class: 12b""") == {'age': 12,
#  'class': '12b',
#  'name': 'Alex Fox'}
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Решение другого пользователя

# def yaml(a):
#     t = [i.strip() for i in a.split('\n') if i]
#     d = {}
#     for elem in t:
#         key, val = (i.strip() for i in elem.split(':'))
#         d[key] = int(val) if val.isdecimal() else val
#     return d


# Задача №14
# лампочка продолжает включатся и выключатся, как и раньше. Но теперь, как результат работы функции,
# я хочу не просто знать, как долго было светло в комнате, а как долго комната была освещена, начиная с определенного
# момента. Добавляется еще один аргумент – start_watching
# , и если он не передан, считаем, как и в предыдущей версии программы, за весь период.

# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    # a1 = els[::]
    # for ind, i in enumerate(a1):
    #     if start_watching:
    #         if i < start_watching:
    #             els.remove(i)
    # if len(els) % 2:
    #     els.insert(0, start_watching)
    # b = [(els[ind + 1] - els[ind]).total_seconds() for ind, i in enumerate(els[:-1])]
    # return int(sum(b[::2]))

#     return sum(
#             (max(start_watching or els[i+1], els[i+1]) -
#              max(start_watching or els[i], els[i])).total_seconds()
#             for i in range(0, len(els), 2)
#         )
#
#
#
# print(
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             datetime(2015, 1, 12, 10, 0, 5),
#         )
#     )


# def checkio(text):
#     print(text.encode().decode('UTF-8'))
#
#
# checkio ( u"предпочтительный" ) == u"предпочтительный"
# checkio ( u"loài trăn lớn" ) == u"loai tran lon"

# import unicodedata
#
# def remove_accents(input_str):
#     nkfd_form = unicodedata.normalize('NFKD', input_str)
#     return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])
#
# print(remove_accents(u"loài trăn lớn"))
# def translate(text: str) -> str:
#     b, i = '', 0
#     while i < len(text):
#         b += text[i]
#         if text[i] in 'aeiouy':
#             i += 3
#         elif text[i] == ' ':
#             i += 1
#         else:
#             i += 2
#     return b
#
# print(translate('hieeelalaooo'))
# assert translate("hieeelalaooo") == "hello"
# assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translate("aaa bo cy da eee fe") == "a b c d e f"
# assert translate("sooooso aaaaaaaaa") == "sos aaa"
# print("Coding complete? Click 'Check' to earn cool rewards!")