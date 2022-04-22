# ДЗ:
# В переменной chess мы получаем какой-то любой фрагмент шахматной партии.
# Например:
# chess = '1. d2 e6 2. e4 d5 3. Кc3 c5 4. Кf3 O-O 5. e:d5 e:d5 6. Сe2 Кf6 7. O-O Сe7 8. Сg5 Кc6 9. d:c5 Сe6 10. Кd4 С:c5 11. Кb3 Сe7 12. Сf3 Кe5 13. Лe1 К:f3+ 14. Ф:f3 Лc8 15. h3 h6'
# 0. Распечатать первый ход партии: 1. d2 e6   Найти как можно больше решений.
# chess = '1. Кd2 Кe6 2. e4 d5 3. Кc3 c5 4. Кf3 O-O 5. e:d5 e:d5 6. Сe2 Кf6 7. O-O Сe7 8. Сg5 Кc6 9. d:c5 Сe6 10. Кd4 С:c5 11. Кb3 Сe7 12. Сf3 Кe5 13. Лe1 К:f3+ 14. Ф:f3 Лc8 15. h3 h6'
#
# # 3. Распечатать на каком ходу у белых была короткая рокировка: O-O.
# chess = chess.split('. O-O')
# print(chess)
# chess = chess[0].split()
# print(chess)
# print(chess[-1])
# print(chess.split('. O-O')[0].split()[-1])

# print(chess.split()[1::3].index('O-O') + 1)

# 4. Распечатать на каком ходу у чёрных была короткая рокировка: O-O.
# chess = chess.split()
# print(chess)
# chess = chess[2::3]
# print(chess)
# print(chess.index('O-O') + 1)

# print(len(chess.split()[2::3][:chess.split()[2::3].index('O-O')+1]))

# print(chess.split()[2::3].index('O-O') + 1)

# if 'O-O' in chess[0]:
#     chess = chess[0]
#     print(chess)
# else:
#     chess = chess[1]
#     print(chess)

# chess = chess.split('. O-O')
# chess = chess[0] if 'O-O' in chess[0] else chess[1]
# chess = chess.split('O-O')
# chess = chess[0].split()
# print(chess[-2].rstrip('.'))

# print(chess)
# print('O-O' in chess[0])
# chess = chess[0].split('O-O')
# chess = chess[0].split()
# print(chess[-2].rstrip('.'))

# 2. Введите текст, слово для поиска и слово замены.
# Программа проверяет, существует ли искомое слово.
# Если да, заменяет это слово заменяющим словом(слово замены) и перепечатывает текст,
# в противном случае он уведомляет вас, что искомое слово не найдено и замены нет.
# s = "У нас, который год, живёт кот, которого Васькой зовут, вот такой кот."
# # кот -> пёс
# print(s)
# print('пес'.join(s))
# s = "У нас, который год, живёт кот, которого Васькой зовут, вот такой кот.".split()
# a = 'кот'
# b = 'пес'
# c = []
# for i in s:
#    if i.replace(',','').replace('.', '') in a and len(i.replace(',','').replace('.', '')) == 3:
#        i = b
#    c.append(i)
# print(c)



 # 2. Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это чисо, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO
# в противном случае. После нескольких заданных вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август

# Входные данные
# Первая строка входных данных содержит число n — наибольшее число,
# которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
#
# Наконец, последняя строка входных данных содержит одно слово HELP.
#
# Выходные данные
# Вы должны вывести все числа, которые мог задумать Август.
# Примеры
# входные данные:
# До какого числа? 10
# Введите числа: 1 2 3 4 5
# Правильно? YES
# Введите числа: 2 4 6 8 10
# Правильно? NO
# Введите числа: HELP
#
# выходные данные:
# 1, 3, 5
# n = int(input(':'))
# numbers = set(range(1, n + 1))
# while True:
#     beat = input('Введите числа:')
#     if beat == 'HELP':
#         break
#     beat = set([int(i) for i in beat.split()])
#     answer = input('Введите ответ:')
#     if answer == 'YES':
#         numbers = numbers.intersection(beat)
#     else:
#         numbers = numbers.difference(beat)
# print(*numbers)

# ДЗ:
# 1. Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают 5000.
#
# a = b = 1
# c = []
# for i in range(1, 20):
#     a, b = b, a + b
#     if not a % 2:
#        c.append(a)
# print(sum(c))

# 4. Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
# Попробуем написать подобную систему.
# На вход программе первой строкой передаётся количество d известных нам слов,
# после чего на d строках указываются эти слова.
# Затем передаётся количество s строк текста для проверки, после чего s строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
# 4
# champions
# we
# are
# Repik
# 3
# We are the champignons
# We Are The Champions
# Repic
#
# Sample Output:
# repic
# champignons
# the

# a = int(input('Количество слов:'))
# d = [input('Слова: ').lower() for _ in range(a)]
# b = int(input('Количество текста:'))
# s = ' '.join([input('Текс для проверки: ').lower() for _ in range(b)]).split()
# c = [i for i in set(s) if i not in d]
# print(*c, sep='\n')


# chess = '1. Кd2 Кe6 2. e4 d5 3. Кc3 c5 4. Кf3 O-O 5. e:d5 e:d5 6. Сe2 Кf6 7. O-O Сe7 8. Сg5 Кc6 9. d:c5 Сe6 10. Кd4 С:c5 11. Кb3 Сe7 12. Сf3 Кe5 13. Лe1 К:f3+ 14. Ф:f3 Лc8 15. h3 h6'
# 4. Распечатать на каком ходу у чёрных была короткая рокировка: O-O.
# chess = chess.split()
# print(chess)
# chess = chess[2::3]
# print(chess)
# print(chess.index('O-O') + 1)

# print(len(chess.split()[2::3][:chess.split()[2::3].index('O-O')+1]))

# print(chess.split()[2::3].index('O-O') + 1)

# if 'O-O' in chess[0]:
#     chess = chess[0]
#     print(chess)
# else:
#     chess = chess[1]
#     print(chess)

# chess = chess.split('. O-O')
# chess = chess[0] if 'O-O' in chess[0] else chess[1]
# chess = chess.split('O-O')
# chess = chess[0].split()
# print(chess[-2].rstrip('.'))

# print(chess)
# print('O-O' in chess[0])
# chess = chess[0].split('O-O')
# chess = chess[0].split()
# print(chess[-2].rstrip('.'))

# 3. Введите любой текст и искомое слово. Программа находит,
# есть ли в тексте искомое слово и выдает ответ «Слово не найдено» или «Слово первый раз встретилось на ... позиции».
# Например:
# s = "У нас, который год, живёт кот, которого Васькой зовут, отличный кот-мышелов, вот такой кот."
# word = "кот"
# # > Слово первый раз встретилось на 26 позиции
# s = "У нас, суперкот, который год, живёт кот, которого Васькой зовут, отличный кот-мышелов, вот такой кот."
# b = "кот"
# s = s.split()
# # print(s)
# # print(s.index('кот,'))
# for i in s:
#     if i.strip(',.') == b:
#         s[s.index(i)] = 'пес'
# print(s)
# x = 12345
# x = str(x)
# # print(x[-3:])
# # print(x[:-3])
#
# s = '12345'
# a = [int(i) for i in s]
# if sum(a[:-3]) == sum(a[-3:]):


# def super_sum(*x):
#     return sum(x)

# def cats(x):
#     return ('cat' * x)
#
#
# # print(my_max(5, 7))
# # print(super_sum(5, 6, 7, 8))
# print(cats(20))
# cats(10)

# def func(name, *mark, math, phizika):  # именованные аргументы всегда пишем последними
#     print(name, ':', *mark)
#     print(math, phizika)
#
# def func2(name, *mark, **pred):  # именованные аргументы всегда пишем последними
#     print(name, ':', *mark)
#     # print(pred)
#     print(*[f'{i} - {pred[i]}' for i in pred], sep='\n')
#     print('Ему в музыканты!' if 'music' in pred else 'Скрипку не давать!')
#
#     # if 'music' in pred:
#     #     print('Ему в музыканты!')
#     # else:
#     #     print('Скрипку не давать!')
#
#
# func('Alex', 20, 30, math=5, phizika=4)
# func2('Alex', 20, 30, math=5, phizika=4, him=5)



# def voc(*bit):
#     for i in bit:
#         for j in bit:
#             print([f'{i * j}' for i in bit for j in bit])
#             break
#
# voc(1, 2, 3, 4, 5 )

# def my_max(a, b):
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     return a if a > b else b
# print(my_max(8, 15))


# 2. Необходимо написать функцию, которая вернёт сумму всех элементов списка до n умноженных на свой индекс.
# Для пустого списка возвращаем 0.
# Пример: n = 5, index_multiplier([1, 2, 3, 4, 5]) ➞ 40.

# n = input('Введите число: ')
# a = []
# b = []
# for ind, i in enumerate(range(1, int(n) + 1)):
#     if n != '':
#         a.append(i)
#         b.append(i * ind)
#     print(b)
# else:
#     print('0')

# x = {1: 'one', 2: 'two'}
# y = {True: 'cat', False: 'dog'}
# z = x | y  # python >= 3.9
# # z = {**x, **y}  # объединение словарей
# print(z)

# x = {'a': 1, 'b': 2, 'c': 3}
# y = {'d': 4, 'f': 5, 'n': 6}
# z = {**x, **y}
# print(z)
# print(*z.values())
# print(z.get('m'))
# print(z.setdefault('m', 7))
# print(*z.keys())
# print(*z.items())
# z.update({'s': 8})
# print(z)
# del z['c']
# print(z)
# g = z.pop('q', 10)
# print(z, g)
# h = z.popitem()
# print(z, h)

# print(week['Выходной'])  # возвращает значение по ключу, применяем, когда уверены в наличие ключа
# print(week.get(2, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - None или Значение
# которое указали во втором параметре
# print(week.setdefault(5, "Пятница"))  # возвращает значение по ключу, если ключа нет - создаст его
# print(week.keys())  # возвращает все ключи
# print(*week.values(), sep='\n')  # возвращает все значения
# print(*week.items(), sep='\n')  # возвращает (ключ, значение)
# print(week)
# week.update({6: 'Суббота'})  # добавляет элемент(ы) словаря
# week[7] = 'Воскресенье'
# print(week)
# del week[1]  # удаляет элемент по ключу
# print(week)
# d = week.pop(44, 'Значение по умолчанию')  # удаляет элемент по ключу и возвращает его значение, если ключа нет,
# то возвратит значение по умолчанию
# print(week, d)
# week2 = week.copy()  # копия словаря
# week2.clear()  # очистить словарь
#
# d1 = {'a': 1, 'b': 2, 'c': 3}
# item = d1.popitem()  # удаляет и возвращает последнюю пару (ключ, значение) python >= 3.7
# print(d1, item)
# print(week)

# id_users = {
#     12: 'Alex',
#     42: 'Alice',
#     82: 'Bob'
# }
# id_users.update({52: 'Vika'})
#
# z = {32: 'bob', 48: 'set', 33: 'dilan', 15: 'sonia'}
# for i in z:
#     id_users.update({i: z[i]})
#
# user = 15
# print(f'Привет {id_users.get(user, "незнакомец")}')


# def nod(x, y):
#     while x and y:
#         if x > y:
#             x = x % y
#         else:
#             y = y % x
#     return x + y

# def nod(x, y):
#     while x != 0:
#         x, y = y % x, x
#     return y
#
#
# print(nod(12, 8))

# def ask_ok(prompt, retries=3, reminder='Попробуй ещё раз!'):
#     while True:
#         ok = input(prompt).lower()
#         if ok == 'yes':
#             return True
#         elif ok == 'no':
#             return False
#         retries -= 1
#         if retries == 0:
#             raise ValueError('Закончились попытки!')
#         print(reminder)
#
# q = ask_ok('Хотите выйти из программы? ')
# # q = ask_ok('Хотите выйти из программы? ', 2)
# # q = ask_ok('Хотите выйти из программы? ', 4, 'Ответ должен быть yes или no!')
# if q:
#     print('Выходим из программы')
# else:
#     print('Остаёмся в программе')


# def sof(a, b=3):
#     while True:



# for i in range(10):
#     line = ''
#     for j in range(10):
#         if i == j:
#             break
#         line += '{}'.format(j)
#     print(line)

# letters = [1, 2, 3]
# my_iter = iter(letters)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print("Привет\'s d")
# b = 5
# try:
#     a = b / 0
# except AssertionError:
#     print('1')
# except AssertionError:
#     print('2')
# except AssertionError:
#     print('3')
# except AssertionError:
#     print('4')
# except AssertionError:
#     print('5')
# b = 5
# try:
#     a = b / 0
# except AssertionError:
#     print('1')
# except AssertionError:
#     print('2')
# except AssertionError:
#     print('3')
# except AssertionError:
#     print('4')
# except AssertionError:
#     print('5')

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
#
# a = A()
# b = B()
# c = C()
#
# print(type(c) == B)
# print(type(b) == C)
# print(type(b) == A)
# print(type(a) == A)
# print(type(a) == B)
# print(type(c) == A)


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


# def frequency_sort(items):
#     # your code here
#     # b = []
#     # c = []
#     # for i in items:
#     #     if i not in b:
#     #         b.append(i)
#     # for j in b:
#     #     c.extend([j] * items.count(j))
#     return sorted(sorted(items, key=items.index), key=items.count, reverse=True)
#
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
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# numbers = [3, 4, 11, 13, 11, 4, 4, 7, 3]
# print(sorted(sorted(numbers), key=numbers.count, reverse=True))
# #
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

#
# from typing import Iterable
#
#
# def except_zero(items: list) -> Iterable:
#     # your code here
#
#     b =  [i for i in sorted(items) if i != 0]
#     for ind, i in enumerate(items):
#         if i == 0:
#             b.insert(ind, 0)
#     return b
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
#     assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
#     assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
#     assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
#     assert list(except_zero([0, 0])) == [0, 0]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#

# checkio(1, 2, 3) == 2
# checkio(5, -5) == 10
# checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
# checkio() == 0

# a = (5, -5)
# print(max(a) - min(a))



# ("Bananas, give me bananas!!!", {"banana", "bananas"}) = 2
# a = "Bananas, give me bananas!!!".lower()
# b = {"banana", "bananas"}
# print(sum(a.count(i) for i in b))

# words_order ( 'привет, мир, я здесь' , [ 'мир' , 'здесь' ] ) == True
# words_order ( 'привет, мир, я здесь' , [ 'здесь' , 'мир' ] ) == False
# words_order ( 'привет, мир, я здесь' , [ 'мир' ] ) == True
# words_order ( 'привет, мир, я здесь' ,
#  [ 'мир' , 'здесь' , 'привет' ] ) == False
# words_order ( 'привет, мир, я здесь' ,
#  [ 'мир' , 'я' , 'здесь' ] ) == Истина
# words_order ( 'привет, мир, я здесь' ,
#  [ 'мир' , 'привет' , 'здесь' ] ) == False
# words_order ( 'привет, мир, я здесь' , [ 'мир' , 'мир' ] ) == False
# words_order ( 'привет, мир, я здесь' ,
#  [ 'страна' , 'мир' ] ) == Ложь
# words_order ( 'привет, мир, я здесь' , [ 'wo' , 'rld' ] ) == False
# words_order ( '' , [ 'мир' , 'здесь' ] ) == False

# a = 'привет, мир, я здесь'.split()
# b = [ 'здесь' , 'мир' ]
# for i in a:
#     if i.rstrip(',') in b:
#         print(a.index(i))

# checkio(123405) == 120
# checkio(999) == 729
# checkio(1000) == 1
# checkio(1111) == 1

# В этой миссии вам нужно создать функцию проверки пароля.
#
# Это условия проверки:
#
# длина должна быть больше 6;
# должен содержать хотя бы одну цифру.
# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == False
# is_acceptable_password('ashort') == False
# is_acceptable_password('muchlonger5') == True
# is_acceptable_password('sh5') == False

# a = "muchlonger5"
# # for i in a:
# #     if i.isdigit() and len(a) > 6:
# print(sum(1 for i in a if i.isdigit()))
#
# def is_acceptable_password(a):
#
#     return len(a) > 9 and 'password' not in a.lower() or len(a) > sum(1 for i in a if i.isdigit()) > 0 and len(a) > 6
#
#
#
#
# if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password("short") == False
    # assert is_acceptable_password('short') == False
    # assert is_acceptable_password('short54') == True
    # assert is_acceptable_password('muchlonger') == True
    # assert is_acceptable_password('ashort') == False
    # assert is_acceptable_password('muchlonger5') == True
    # assert is_acceptable_password('sh5') == False
    # assert is_acceptable_password('1234567') == False
    # assert is_acceptable_password('12345678910') == True
    # assert is_acceptable_password('password12345') == False
    # assert is_acceptable_password('PASSWORD12345') == False
    # # assert is_acceptable_password('pass1234word') == True
    # print("Coding complete? Click 'Check' to earn cool rewards!")
#
# def is_all_upper(text: str) -> bool:
#     # if text and text.isspace() != True:
#     # return text == text.upper() if text.isalpha() else False
#     # else:
#     #     return False
#
#
#     # if text:
#     return False if text.isspace() or text != True or text.isdigit() else text == text.upper()
#     # else:
#     #     return False
#
# if __name__ == "__main__":
#     print("Example:")
#     print(is_all_upper("ALL UPPER"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_all_upper("ALL UPPER") == True
#     assert is_all_upper("all lower") == False
#     assert is_all_upper("mixed UPPER and lower") == False
#     assert is_all_upper("") == False
#     assert is_all_upper(" ") == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# verify_anagrams('Programming', 'Gram Ring Mop') == True
# verify_anagrams('Hello', 'Ole Oh') == False
# verify_anagrams('Kyoto', 'Tokyo') == True


# a = 'Kyoto'.lower()
# b = 'Tokyo'.replace(' ','').lower()
# for i in b:
#     if i in a and len(a) == len(b):
#         print(12)
# import itertools
# import json
# import time
# #
# # start = time.time()  # текущее время в секундах с начала цифровой эры
# # print(start)
# # for i in range(1_000_000):
# #     x = i ** 3
# # end = time.time() # текущее время окончания работы программы
# # print(end)
# # print(end - start)
# # end = time.time()
# # print(time.ctime(time.time()))  # Mon Jan 24 21:04:41 2022
# # # time.sleep(3)  # остановка программы в секундах
# # print(time.ctime())  # показывает текущую дату-время
# #
# # print(time.localtime())  # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=24, tm_hour=21, tm_min=9, tm_sec=18, tm_wday=0, tm_yday=24, tm_isdst=0)
# # print(time.localtime().tm_year)
# # print(time.localtime().tm_mon)
# # print(time.strftime('Today is %B %d, %Y.', time.localtime()))
# # print(time.monotonic())  # таймер независимый от внешних условий (время с запуска программы) в секундах
# # # print(time.ctime(time.monotonic()))
# # seconds = 1613585177.8484533
# # t = time.localtime(seconds)
# # print(t)
# # s = time.mktime(t)  # переводит в секунды struct_time
# # print(s)
# # print(time.time())
# # print(time.mktime(time.localtime()))
# # print(time.timezone)  # смещение местного часового пояса в секундах  (-7200)
# # print(time.tzname)  # кортеж их двух строк (имя часового пояса, имя местного часовго пояса) ('Финляндия (зима)', 'Финляндия (лето)')
#
# # import time
# # # Спрашиваем текст напоминания, который нужно потом показать пользователю
# # # Ждём ответа пользователя и результат помещаем в строковую переменную text
# # text = input("О чём вам напомнить?: ")
# # # Спрашиваем про время
# # # Тут будем хранить время, через которое нужно показать напоминание
# # local_time = float(input("Через сколько минут?: "))
# # # Переводим минуты в секунды
# # local_time = local_time * 60
# # # Ждём нужное количество секунд, программа в это время ничего не делает
# # time.sleep(local_time)
# # # Показываем текст напоминания
# # print(text)
#
#
# import time
#
# # def fun():
# #     sec = 0
# #     while True:
# #         print(sec)
# #         time.sleep(1)
# #         sec += 1
# #
# # while True:
# #     a = input('1 начало отсчета, 2 конец отсчета')
# #     if a == '1':
# #         fun()
# #     elif a == '2':
# #         break
#
# # Отображаем инструкцию для пользователя
# # print('Нажмите клавишу Enter, чтобы начать. После этого нажмите клавишу Enter, чтобы "нажать" на секундомер. \n'
# #       'Нажмите комбинацию клавиш Ctrl-C для останова секундомера и выхода из программы.')
# # # input()
# # print('Начали.')
# # startTime = time.time() # стартовое время первого круга
# # lastTime = startTime
# # lapNum = 1
# # #
# # # Начало отслеживание круга
# # try:
# #     while True:
# #         input()
# #         lapTime = round(time.time() - lastTime, 5)
# #         print(time.time())
# #         print(lastTime)
# #         totalTime = round(time.time() - startTime, 2)
# #         print('Круг #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
# #         lapNum += 1
# #         lastTime = time.time() # сброс времени последнего круга
# # except KeyboardInterrupt:
# #     # Обработать исключение Ctrl-C, чтобы не отображалось сообщение об ошибке
# #     print('\nГотово.')
#
# #
# # now = time.monotonic()
# # t1 = time.time()
# # delta1 = t1 - now
# # print('delta1=', delta1)
# # print(now, t1)
# # for i in range(2_000_000):
# #     x = i ** 3
#
#
# # print(time.ctime(now))
# # print(time.ctime(time.time()-now))
# # t2 = time.time()
# # now2 = time.monotonic()
# # delta2 = t2 - now2
# # print(now2 - now)
# # print(t2 - t1)
# # print('delta2=', delta2)
#
# # yaml('name: Alex
# # age: 12') == {'age': 12, 'name': 'Alex'}
# # a = 'name: Alex\nage: 12'.replace('\n', ', ')
# # a = '''{"name": "Alex", "age": 12}'''
# # #
# # # # a1 = eval(a)
# # # print(a)
# # a1 = json.loads(a)
# # print(type(a1))
# # a = '''{"a": [1, 2, 3], "b": 12345, "c": true, "123": null}'''
# # a1 = json.loads(a)
# # print(a1)
#
# # with open('my_json', 'w', encoding='UTF-8') as proba:
# #     json.dump(a, proba, indent=3)
# #
# # with open('my_json', 'r', encoding='UTF-8') as proba:
# #     a = json.load(proba)
# # a1 = json.loads(a)
# # print(type(a1))
#
#
#
# # d = {'a': [1, 2, 3], 'b': 12345, 'c': True, 123: None}
# # s = json.dumps(d)  # преобразует словарь в json-строку
# # print(s)
# # s2 = json.loads(s)  # преобразует json-строку в словарь
# # print(s2)
#
# # json.dump(s, file)  # записывает объект json s в файл file
# # s3 = json.load(file)  # загуржает json из файла file
#
# # repr()  преобразует словарь в строку
# # eval()  преобразует строку в словарь
# # d2 = repr(d)
# # print(d2, type(d2))
# #
# # d3 = eval(d2)
# # print(d3, type(d3))
#
# # CSV файлы хранят информацию в табличном формате
# # f.writerow(s) записывает обьект s в файл f
# # f.writerows(s) записывает итерируемый обьект s в файл f
# # csv.writer создаем обьект который записывает данные в cvs файлы по каким-то параметрам
# # delimiter - разделитель, то чем будут оазделяться элементы
# # quoting=csv.QUOTE_ALL помещает значения в кавычки
# # newline='' пишим стандартно не меняя
# # csv.reader(f) создает обьект который будет читать наш файл
# # csv.DictWriter если нужно записать словарь
# # fieldnames= параметр при создании словарей в который передаем название колонок
# # csv.DictReader(f) создает обьект который будет читать наш файл для словарей
# import csv
# # users = [
# #     {'name': 'Tom', 'age': 27},
# #     {'name': 'Alice', 'age': 35},
# #     {'name': 'Jerry', 'age': 17},
# # ]
# #
# # my_csv = 'dict.csv'
# # with open('my_csv', 'w', newline='') as proba:
# #     columns = list(users[0].keys())
# #     my_file = csv.DictWriter(proba, fieldnames= columns)
# #     my_file.writeheader()
# #     my_file.writerows(users)
#
#
# # user = {'name': 'Mikky', 'age': 5}
# # with open('my_csv', 'a', newline='') as proba:
# #     columns = list(user.keys())
# #     my_file = csv.DictWriter(proba, fieldnames= columns)
# #     my_file.writerow(user)
#
#
#
#
# # data = [
# #     ['Tom', 28],
# #     ['Jerry', 20],
# #     ['Alice', 25]
# # ]
# # # my_csv = 'my_csv.csv' для чего???
# # with open('my_csv', 'w', newline='') as proba:
# #     my_file = csv.writer(proba, delimiter=',', quoting=csv.QUOTE_ALL)
# #     my_file.writerows(data)
#
# # days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# # days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# # days_diff((2014, 8, 27), (2014, 1, 1))
# from datetime import date, datetime, timedelta
# # a = (2014, 8, 27)
# # b = (2014, 1, 1)
# # print(abs(date(b[0], b[1], b[2]) - date(a[0], a[1], a[2])).days)
#
# # my_date2 = date(2022, 4, 28)
# # my_date3 = date(2021, 1, 24)
# # date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# # date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# # date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# # time  = "11.04.1812 01:01"
# # d = datetime.strptime(time, '%d.%m.%Y %H:%M')
# # c = d.strftime('%#d, %B, %Y, %#H, %#M').split(', ')
# # print(c)
# #
# # a = 's'
# # b = 's'
# #
# # if c[3] == '1' and c[4] != '1':
# #     a = ''
# # elif c[4] == '1' and c[3] != '1':
# #     b = ''
# # elif c[3] and c[4] == '1':
# #     a = ''
# #     b = ''
# # # print(c[0].lstrip('0'), c[1], c[2], 'year', c[3].replace('0', '', 1), 'hour' + a, c[4].replace('0', '', 1), 'minute' + b)
# # print(c[0], c[1], c[2], 'year', c[3], 'hour' + a, c[4], 'minute' + b)
# # from datetime import datetime
# # def date_time(time: str) -> str:
# #     time = datetime.strptime(time, '%d.%m.%Y %H:%M')
# #     c = time.strftime('%#d, %B, %Y, %#H, %#M').split(', ')
# #     a = 's'
# #     b = 's'
# #     if c[3] == '1':
# #         a = ''
# #     elif c[4] == '1':
# #         b = ''
# #     elif c[3] and c[4] == '1':
# #         a = ''
# #         b = ''
# #     return f'{c[0]} {c[1]} {c[2]} year {c[3]} hour{a} {c[4]} minute{b}'
# #
# # if __name__ == "__main__":
# #     print("Example:")
# #     print(date_time("01.01.2000 00:00"))
# #
# #     # These "asserts" using only for self-checking and not necessary for auto-testing
# #     assert (
# #         date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"
# #     ), "Millenium"
# #     assert (
# #         date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
# #     ), "Victory"
# #     assert (
# #         date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
# #     ), "Somebody was born"
# #     print("Coding complete? Click 'Check' to earn cool rewards!")
# #
#
# # a = timedelta(days=5, hours=21, minutes=2, seconds=37)
# # %a день недели соращённый Sun, Mon...
# # %A день недели полный Sunday, Monday...
# # %w день недели как десятичное число, где 0 - воскресенье...
# # %d день месяца в формате двух цифр 01, 02... 31
# # %b месяц сокращённый Jan, Feb...
# # %B месяц полный January, Fedruary...
# # %m номер месяца в формате двух цифр 01, 02...
# # %y последние 2 цифры года 01...99
# # %Y год полностью 0001...9999
# # %H час в 24-часовом формате
# # %I час в 12-часовом формате
# # %p AM или PM
# # %M минуты в формате двух цифр
# # %S секунды в формате двух цифр
# # %f микросекунды в формате 6 цифр
# # %j номер дня в году в формате 3 цифр 001... 366
# # %U номер недели в году 00...53
# # %Z название часового пояса
# # %% знак процента
#
# # time_converter('12:30') == '12:30 p.m.'
# # time_converter('09:00') == '9:00 a.m.'
# # time_converter('23:15') == '11:15 p.m.'
# # a = '23:15'
# # b = datetime.strptime(a, '%H:%M')
# # c = b.strftime('%#I:%M %p').split()
# #
# # c[1:] = [f'{i[0].lower()}.{i[1].lower()}.' for i in c[1:]]
# # print(' '.join(c))
#
# # sum_light([
# #     datetime(2015, 1, 12, 10, 0 , 0),
# #     datetime(2015, 1, 12, 10, 10 , 10),
# # ]) == 610
# # a = [datetime(2015, 1, 12, 10, 0 , 0), datetime(2015, 1, 12, 10, 10 , 10),]
# # b = datetime(2015, 1, 12, 10, 10 , 10) - datetime(2015, 1, 12, 10, 0 , 0)
# # print(b)
# # print(int(b.total_seconds()))
# # a = [datetime(2015, 1, 12, 10, 0 , 0), datetime(2015, 1, 12, 10, 10 , 10), datetime(2015, 1, 12, 11, 0 , 0), datetime(2015, 1, 12, 11, 10 , 10),]
# # b = [(a[ind + 1] - a[ind]).total_seconds() for ind, i in enumerate(a[:-1])]
# # print(int(sum(b[::2])))
#
# # a = [datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10),]
# # b = datetime(2015, 1, 12, 10, 10 , 10) - datetime(2015, 1, 12, 10, 0 , 0)
# # c = None
# # a1 = a[::]
# # for ind, i in enumerate(a1):
# #     if c:
# #         if i < c:
# #             a.remove(i)
# # if len(a) % 2:
# #     a.insert(0, c)
# # b = [(a[ind + 1] - a[ind]).total_seconds() for ind, i in enumerate(a[:-1])]
# # print(int(sum(b[::2])))
#
# # print(int(b.total_seconds()))
# # print(int(d.total_seconds()))
# # sum_light([
# #     datetime(2015, 1, 12, 10, 0, 0),
# #     datetime(2015, 1, 12, 10, 0, 10),
# # ],
# # datetime(2015, 1, 12, 10, 0, 5)) == 5
#
# # sum_light([
# #     datetime(2015, 1, 12, 10, 0, 0),
# #     datetime(2015, 1, 12, 10, 10, 10),
# #     datetime(2015, 1, 12, 11, 0, 0),
# #     datetime(2015, 1, 12, 11, 10, 10),
# # ],
# # datetime(2015, 1, 12, 9, 0, 0),
# # datetime(2015, 1, 12, 10, 5, 0)) == 300
#
# # a = [datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10), datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 12, 11, 10, 10),]
# # # b = datetime(2015, 1, 12, 10, 10 , 10) - datetime(2015, 1, 12, 10, 0 , 0)
# # c = datetime(2015, 1, 12, 9, 0, 0)
# # d = datetime(2015, 1, 12, 10, 5, 0)
# # a1 = a[::]
# # for ind, i in enumerate(a1):
# #     if c:
# #         if i < c:
# #             a.remove(i)
# # if len(a) % 2:
# #     a.insert(0, c)
# # print(a)
# # a2 = a[::]
# # for ind, i in enumerate(a2[1::2]):
# #     if d:
# #         if i > d:
# #             a.remove(i)
# # print(a)
# #
# #
# #
# # b = [(a[ind + 1] - a[ind]).total_seconds() for ind, i in enumerate(a[:-1])]
# # print(int(sum(b[::2])))
#
# # highest_building([[0, 0, 1, 0],
# #                   [1, 0, 1, 1],
# #                   [1, 1, 1, 1],
# #                   [1, 1, 1, 1]]) == [3, 4]
#
# # a = [
# #         [0, 0, 0, 1, 0, 0, 0],
# #         [0, 0, 1, 1, 1, 0, 0],
# #         [0, 1, 1, 1, 1, 1, 0],
# #         [1, 1, 1, 1, 1, 1, 1],
# #         [1, 1, 1, 1, 1, 1, 1],
# #         [1, 1, 1, 1, 1, 1, 1]
# #     ]
# # b = [[i[j] for i in a] for j in range(len(a[0]))]
# # c = [sum(i) for i in b]
# # print([c.index(max(c)) + 1, max(c)])
#
# from itertools import cycle
#
# a = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# b = 3
# c = []
# for i in range(b):
#     for j in a:
#         c.append(j)
# print(c)
# cycle(iterable)
# b = itertools.cycle(a)
# c =[]
# for j in range(1084):
#     c.append(next(b))
# print(max(c, key=c.count))


# print(a.index(min(a, key=a.count)) + 1)

from datetime import date, time, datetime, timedelta

# Constructors
# <D> = date(year, month, day)
# <T> = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
# <DT> = datetime(year=0, month=0, day=0, hour=0, minute=0, second=0, microsecond=0)
# <TD> = timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0)

# Now текущая дата
# <D/DT> = D.DT.today()  # current date
# <DT> = DT.utcnow()
# <DT> = DT.now(<tzinfo>)

# d = datetime.strptime('2020-05-15 22:34:10.00 +0200', '%Y-%m-%d %H:%M:%S.%f %z') # из строки по шаблону формирует обьект datetime
# print(d.strftime('%A, %d of %B %y, %I:%M %p %Z'))  # Friday, 15 of May 20, 10:34 PM UTC+02:00 # из обьекта datetime по шаблону формирует строку

# Arithmetics
# <D/DT> = <D/DT> +- <TD>
# <TD> = <D/DT> - <D/DT>
# <TD> = <DT> - <DT>

# print(datetime.now())  # 2022-01-28 21:18:27.329330
# print(datetime.now().time())  # 21:18:27.329330
# print(datetime.now().date())  # 2022-01-28
#
# my_date = date(2022, 1, 28)
# print(my_date)  # 2022-01-28
# print(date.today())  # 2022-01-28
# print(date.today().weekday())  # 4
#
# my_time = time(21, 23, 40)
# # print(my_time)  # 21:23:40
# #
# # my_datetime = datetime(2022, 1, 28, 22, 12, 43)
# # print(my_datetime)  # 2022-01-28 22:12:43
# my_datetime2 = datetime.combine(my_date, my_time)
# # print(my_datetime2)  # 2022-01-28 21:23:40
# print(my_datetime2.year)  # 2022
# print(my_datetime2.day)  # 2022
# print(my_datetime2.month)  # 2022
# print(my_datetime2.time())  # 2022
#
# delta_time1 = timedelta(weeks=2, seconds=20)
# print(delta_time1)  # 14 days, 0:00:20
# print(delta_time1.days)  # 14
# print(delta_time1.total_seconds())  # 1209620.0
# # # timedelta.total_seconds() переводит разницу времени в секунды
# # a = datetime(2015, 1, 12, 10, 0 , 0)
# # b = datetime(2015, 1, 12, 10, 10 , 10)
# # print(int((b - a).total_seconds()))
# delta_time2 = timedelta(weeks=-4, seconds=-40)
# print(delta_time2)
# a = date(2020, 12, 10)
# b = date(2021, 10, 3)
# c = b - a
# print(type(c))

#
# delta_time3 = timedelta(days=4, hours=12)
# delta_time4 = timedelta(days=1, hours=14)
# print(delta_time3 - delta_time4)  # 2 days, 22:00:00
# print(delta_time3 + delta_time4)  # 6 days, 2:00:00
# print(delta_time4 * 10)  # 15 days, 20:00:00
# print(delta_time4 / 10)  # 3:48:00
# print(delta_time3 / delta_time4)  # 2.8421052631578947
#
# my_date2 = date(2022, 4, 28)
# my_date3 = date(2021, 1, 24)
# delta_time5 = timedelta(days=5, hours=8)
# #
# print(my_date2 + delta_time5)  # 2022-05-03
# print(my_date2 - delta_time5)  # 2022-04-23
# print(my_date2 - my_date3)  # 459 days, 0:00:00
# print(my_date2 > my_date3)  # True
#
# my_date2 = datetime(2022, 4, 28, 15, 20, 45)
# my_date3 = datetime(2021, 1, 24, 12, 12, 12)
# print(my_date2 + delta_time5)  # 2022-05-03 23:20:45
# print(my_date2 - delta_time5)  # 2022-04-23 07:20:45
# print(my_date2 - my_date3)  # 459 days, 3:08:33
# print(my_date2 > my_date3)  # True
#
# print(datetime.now().strftime('%A %d-%B-%y %H:%M:%S'))  # Friday 28-January-22 21:50:33
# print(date.today())
# print(date.today().strftime('%B'))  # January
#
# # # передача кортежа в datetime с помощью распаковки
# a = (1982, 4, 19)
# print(datetime(*a))
# print(date(*a))
# Основные обозначения:
# %a день недели соращённый Sun, Mon...
# %A день недели полный Sunday, Monday...
# %w день недели как десятичное число, где 0 - воскресенье...
# %d день месяца в формате двух цифр 01, 02... 31
# %b месяц сокращённый Jan, Feb...
# %B месяц полный January, Fedruary...
# %m номер месяца в формате двух цифр 01, 02...
# %y последние 2 цифры года 01...99
# %Y год полностью 0001...9999
# %H час в 24-часовом формате, если нужно вывести время без 0 впереди записываем %#H для винды и %-H для линукс
# %I час в 12-часовом формате
# %p AM или PM
# %M минуты в формате двух цифр
# %S секунды в формате двух цифр
# %f микросекунды в формате 6 цифр
# %j номер дня в году в формате 3 цифр 001... 366
# %U номер недели в году 00...53
# %Z название часового пояса
# %% знак процента

# def yaml(a):
#     b = {}
#     for i in a.split('\n'):
#         if i:
#             c, d = i.replace('"', '').split(': ')
#             b[c] = int(d) if d.isdigit() else d
#     return b
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(yaml('name: Alex\nage: 12'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
#     assert yaml('name: Alex Fox\n'
#      'age: 12\n'
#      '\n'
#      'class: 12b') == {'age': 12,
#      'class': '12b',
#      'name': 'Alex Fox'}
#     assert yaml('name: "Alex Fox"\n'
#      'age: 12\n'
#      '\n'
#      'class: 12b') == {'age': 12,
#      'class': '12b',
#      'name': 'Alex Fox'}
#     assert yaml('name: "Alex \\"Fox\\""\n'
#      'age: 12\n'
#      '\n'
#      'class: 12b') == {'age': 12,
#      'class': '12b',
#      'name': 'Alex "Fox"'}
#     assert yaml('name: "Bob Dylan"\n'
#      'children: 6\n'
#      'alive: false') == {'alive': False,
#      'children': 6,
#      'name': 'Bob Dylan'}
#     assert yaml('name: "Bob Dylan"\n'
#      'children: 6\n'
#      'coding:') == {'children': 6,
#      'coding': None,
#      'name': 'Bob Dylan'}
#     assert yaml('name: "Bob Dylan"\n'
#      'children: 6\n'
#      'coding: null') == {'children': 6,
#      'coding': None,
#      'name': 'Bob Dylan'}
#     assert yaml('name: "Bob Dylan"\n'
#      'children: 6\n'
#      'coding: "null" ') == {'children': 6,
#      'coding': 'null',
#      'name': 'Bob Dylan'}
#     print("Coding complete? Click 'Check' to earn cool rewards!")

    # assert yaml('name: "Alex \\"Fox\\""\n'
    #             'age: 12\n'
    #             '\n'
    #             'class: 12b') == {'age': 12,
    #                               'class': '12b',
    #                               'name': 'Alex "Fox"'}

import string
# a = 'name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b'
# # print(a)
#
#
# b = {}
# for i in a.split('\n'):
#     # print(i)
#     for j in i.split(': '):
#         print(j)
    # print(i.strip(string.punctuation).split(': '))
#     if i:
#         c, d = i.replace('"', '').split(': ')
#         b[c] = int(d) if d.isdigit() else d
# print(b)

# import math
# a = ("2014-01-01 01:12:13 181",
#                        "2014-01-02 20:11:10 600",
#                        "2014-01-03 01:12:13 6009",
#                        "2014-01-03 12:13:55 200")
# # # print(a)
# #
# d = {}
# for i in a:
#     b = datetime.strptime(''.join(i.split()[:1]), '%Y-%m-%d')
#     if b in d.keys():
#         d[b] += math.ceil(int(i.split()[-1])/60)
#     else:
#         d[b] = math.ceil(int(i.split()[-1])/60)
#
# print(d)
# b = sum(100 + (d[i] - 100)*2 if d[i] > 100 else d[i] for i in d)
# print(b)

from datetime import datetime
import math
from typing import List
#
#
# def total_cost(calls: List[str]) -> int:
#     d = {}
#     for i in calls:
#         b = datetime.strptime(''.join(i.split()[:1]), '%Y-%m-%d')
#         if b in d.keys():
#             d[b] += math.ceil(int(i.split()[-1]) / 60)
#         else:
#             d[b] = math.ceil(int(i.split()[-1]) / 60)
#
#     return sum(100 + (d[i] - 100) * 2 if d[i] > 100 else d[i] for i in d)
#
#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert total_cost(("2014-01-01 01:12:13 181",
#                        "2014-01-02 20:11:10 600",
#                        "2014-01-03 01:12:13 6009",
#                        "2014-01-03 12:13:55 200")) == 124, "Base example"
#     assert total_cost(("2014-02-05 01:00:00 1",
#                        "2014-02-05 02:00:00 1",
#                        "2014-02-05 03:00:00 1",
#                        "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
#     assert total_cost(("2014-02-05 01:00:00 60",
#                        "2014-02-05 02:00:00 60",
#                        "2014-02-05 03:00:00 60",
#                        "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
#
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
# ],
# datetime(2015, 1, 12, 10, 10, 0),
# datetime(2015, 1, 12, 11, 0, 10)) == 20
# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
#     return sum(
#         (max(start_watching or els[i + 1], els[i + 1]) -
#          max(start_watching or els[i], els[i])).total_seconds()
#         for i in range(0, len(els), 2)
#     )
#
# print(
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 11, 0, 0),
#         ))
# if __name__ == "__main__":
#     print("Example:")
#     print(
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             datetime(2015, 1, 12, 10, 0, 5),
#         )
#     )
#
#     assert (
#         sum_light(
#             els=[
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             start_watching=datetime(2015, 1, 12, 10, 0, 5),
#         )
#         == 5
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 0, 10),
#             ],
#             datetime(2015, 1, 12, 10, 0, 0),
#         )
#         == 10
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 11, 0, 0),
#         )
#         == 610
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 11, 0, 10),
#         )
#         == 600
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#             ],
#             datetime(2015, 1, 12, 10, 10, 0),
#         )
#         == 620
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#                 datetime(2015, 1, 12, 11, 10, 11),
#                 datetime(2015, 1, 12, 12, 10, 11),
#             ],
#             datetime(2015, 1, 12, 12, 10, 11),
#         )
#         == 0
#     )
#
#     assert (
#         sum_light(
#             [
#                 datetime(2015, 1, 12, 10, 0, 0),
#                 datetime(2015, 1, 12, 10, 10, 10),
#                 datetime(2015, 1, 12, 11, 0, 0),
#                 datetime(2015, 1, 12, 11, 10, 10),
#                 datetime(2015, 1, 12, 11, 10, 11),
#                 datetime(2015, 1, 12, 12, 10, 11),
#             ],
#             datetime(2015, 1, 12, 12, 9, 11),
#         )
#         == 60
#     )
#
#     print("The second mission in series is done? Click 'Check' to earn cool rewards!")

# assert words_order("hi world im here", ["here", "world"]) == False
# words_order("hi world world im here",["world","world"])
# words_order("hi world world im here hi world world im here",["world","here"])
# assert words_order("hi world im here", ["world", "here"]) == True


# a = "hi world im here".split()
# # print(a)
# b = ["world", "here"]
# print(a.index(b[0]))
# print(a.index(b[1]))
# for ind, i in enumerate(b[:-1]):
#     if i in a:
#         if a.index(b[ind]) - a.index(b[ind+1]) < 0:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)
# d = []
# for i in c:
#     if i in b:
#         d.append(i)
# print(d)

# d = [i for i in c if i in b]

# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# if [i for i in c if i in b] == b:
#     print(True)
# def words_order(text: str, words: list) -> bool:
#     c = []
#     for i in text.split():
#         if i not in c:
#             c.append(i)
#     return [i for i in c if i in words] == words
# print(words_order("hi world im here", ["world", "here"]))

import matplotlib.pyplot as plt
# a = plt.figure()
# b = a.add_subplot(111)
# b.set_title('Времена года', color='blue', size=30)
# b.set(xticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], yticks=[])
# b.set_xlabel('Месяцы', color='red', size= 15)
# b.set_ylabel('Дни',color='red', size= 15 )
# b.set_facecolor('yellow')


# a = plt.figure()
# winter = a.add_subplot(4, 1, 1)
# spring = a.add_subplot(4, 1, 2)
# summer = a.add_subplot(4, 1, 3)
# autumn = a.add_subplot(4, 1, 4)
# winter.set_facecolor('blue')
# winter.set_title('winter', color='blue', size=10)
# winter.set(xticks=[], yticks=[])
# spring.set_facecolor('yellow')
# spring.set_title('spring', color='yellow', size=10)
# spring.set(xticks=[], yticks=[])
# summer.set_facecolor('green')
# summer.set_title('summer', color='green', size=10)
# summer.set(xticks=[], yticks=[])
# autumn.set_facecolor('orange')
# autumn.set_title('autumn', color='orange', size=10)
# autumn.set(xticks=[], yticks=[])
# plt.show()

#
# checkio ( u"""МЕЧТАЮ яблоки на стене,
# И снится часто, милый,
# Мне приснилось, что если я все пересчитаю,
# -Сколько появится?""" , u"десять" ) == [ 2 , 14 , 2 , 16 ]
from pprint import pprint
from itertools import zip_longest

# checkio(u"""DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", u"ten") == [2, 14, 2, 16]
# a = """DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?"""
# b = "ten"
# a = a.replace(' ', '').lower().splitlines()
# for i in a:
#     # print(i)
#     if b in i:
#         print(a.index(i) + 1)
#         print(i.index(b) +1)
#         print(i.index(b) + len(b))


#
# a = """He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""" .replace(' ', '').lower().splitlines()
# b = "noir"
# # [4, 16, 7, 16]
# # pprint(a)
# a2 = [list(i) for i in a]
# # pprint(a2)
# c = list(zip_longest(*a2, fillvalue=' '))
# print(c)
# for i in c:
#     k = ''.join(i)
#     if b in k:
#         print(c.index(i) + 1)
#         print(k.index(b) +1)
#         print(k.index(b) + len(b))
# a = [5, 7, 10, 4, 2, 9, 10, 1, 3]
# a += [float('-inf')]
# # b = [-1] + [ind for ind, i in enumerate(a[:-1]) if i > a[ind + 1]] + [len(a)]
# # print(b)
# # c = [a[i + 1:b[ind + 1] + 1][::-1] for ind, i in enumerate(b[:-1])]
# # print(sum(c, []))
# b = 0
# c = []
# for ind, i in enumerate(a[:-1]):
#     if i > a[ind + 1]:
#         c.extend(a[b:ind + 1])
#         b = ind + 1
# # print(c + a[b:])
# print(c)
# print(float('-inf')) # минус бесконечность(какое-то число которое меньше любого елемента в списке)
# print(float('inf')) # бесконечность(какое-то число которое , больше любого елемента в списке)

# Даны два списка A и B одинакового размера. Сформировать новый список C того же размера, каждый элемент которого равен произведению из элементов массивов A и B с тем же индексом.
# Например: a = [1, 2, 3, 4]   b = [5, 6, 7, 8]  -> c = [5, 12, 21, 32]

# Дан список чисел. Найти максимальное количество четных чисел в наборе, идущих подряд.
# s = [1, 7, 0, 5, 4, 9, 8, 4, 2, 1, 2, 4] #  -> 3

# Дан набор содержащий только нули и единицы.Найти количество элементов
# в самой длинной последовательности одинаковых чисел.
# s = [ 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]   -> 4


from itertools import groupby, islice, starmap
# things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
# for  x, y in groupby(things, lambda x: x[1]+x[0]):
# print({x: next(y) for  x, y in groupby(things, lambda x: x[1]+x[0])})
# print({x: tuple(*y) for  x, y in groupby(things, lambda x: x[1]+x[0])})

# itertools.islice(iterable[, start], stop[, step]) - итератор, состоящий из среза.
# x = (i for i in range(2, 8))
# print(list(islice(x, 0, 4)))

# itertools.starmap(function, iterable) - применяет функцию к каждому элементу последовательности (каждый элемент распаковывается).
# print(*starmap(lambda x,y: x * y, [(2,5), (3,2), (3,10)]))  # -> 32 9 1000

# create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
# create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
# a = [1, 2, 3, 4, 5, 7, 8, 12]
# b = []
# for ind, i in enumerate(a[:-1]):
#     if a[ind] - a[ind + 1] == -1:
#         b.append(i)
# print(b)


# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 3),
#     (datetime(2015, 1, 12, 10, 1, 20), 3),
# ]) == 60

# a = datetime(2015, 1, 12, 10, 0, 50)
# b = datetime(2015, 1, 12, 10, 1, 0)
# print((b-a).total_seconds())

# a = [
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 3),
#     (datetime(2015, 1, 12, 10, 1, 20), 3),
# ]
# b = []
# for i in a:
#     if type(i) == tuple:
#         b.append(i[0])
#     else:
#         b.append(i)
# pprint(b)
# print(min(b))
# print(max(b))
# print((max(b)-min(b)).total_seconds())

# from itertools import zip_longest

# for a1, a2 in zip_longest(*[iter(a)]*2, fillvalue=0):
#     print(a1)
#     print(a2)
#
# c = list(zip_longest(*[iter(a)], fillvalue=0))
# pprint(c)
# print(round(6.5))

# ан список из строк. Создайте однострочное решение (при помощи list comprehension),
# которое приведёт к верхнему регистру все строки, содержащие слово 'price')
# a = ['hello world', 'is it price', 'where is price', 'what is your name']
# print([i.upper() if 'price' in i else i for i in a])


# ДЛЯ БД
# with open('products.csv', 'r', encoding='UTF-8') as f:
#     x = f.readlines()
# pprint(tuple(tuple(i.rstrip().split(',')) for i in x))


# import csv
# with open('products.csv', 'r', newline='') as f:
#     x = csv.reader(f)
#     pprint(tuple(tuple(i) for i in x))
# a = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# b = 'роскомнадзор'
# c = b + ' ' + 'запретил букву'
#
# while c:
#     d = ''
#     for i in c:
#         for j in range(len(a)):
#             if a[j] in c:
#                 c = c + ' ' + a[j]
#                 break
#         if c[-1]!= i:
#             d += i
#     c = d
#     print(c + ' ' +  a[j])


# for i in a:
#     if i != 'а':
#         b += i
# print(b)




a, b = input(), input()
if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
    print('оранжевый')
elif a =='синий' and b == 'желтый' or b =='синий' and a == 'желтый':
    print('зеленый')
elif a == b == 'красный':
    print('красный')
elif a == b == 'синий':
    print('синий')
elif a == b == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')











