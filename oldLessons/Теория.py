# print('Hello, world!')
# a = 12  # int целые числа
# b = 3.1415926  # float дробные числа
# c = "text 23"  # str строка
# d = [2, 5.78, 'apple', [1, 2]]  # list список
# d[2] = "cat"
# d[3][0] = 9
# print(d)
# d[3][1] = "fff"
# print(d)
# e = (4, 7.8, 'cat')  # tuple кортеж
# f1 = True  # bool логический тип
# f2 = False
# g = {2, 6.7, 'dog'}  # set множество
# s = [2, 4, 4, 6, 6, 2]
# print(set(s))
# print(set('apple'))
# h = {'key': 'value', 'Alice': [8, 6, 9, 8]}  # dict словарь
# print(h['Alice'])

# import math
#
# # print(math.cos(math.pi))
# num1 = math.sqrt(2)     # вычисление корня квадратного из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз

from math import *  # позволяет не писать название модуля и символ точки. При таком способе подключения,
                    # импортируются абсолютно все функции модуля math.

# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# Список функций модуля math
#
# Округления
# int()	Округляет число в сторону нуля
# round(x)	Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до
            # ближайшего четного числа
# round(x, n)	Округляет число x до n знаков после точки
# floor(x)	Округляет число x вниз («пол»)
# ceil(x)	Округляет число x вверх («потолок»)
# abs(x)	Модуль числа x (абсолютная величина)

# Корни, логарифмы, степени и факториал

# sqrt(x)	Квадратный корень числа x
# pow(x, n)	Возведение числа x в степень n
# log(x)	Натуральный логарифм числа x. Основание натурального логарифма равно числу e
# log10(x)	Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
# log(x, b)	Логарифм числа x по основанию b
# factorial(n)	Факториал натурального числа n

# Тригонометрия

# degrees(x)	Преобразует угол x, заданный в радианах, в градусы
# radians(x)	Преобразует угол x, заданный в градусах, в радианы
# cos(x)	Косинус угла x, задаваемого в радианах
# sin(x)	Синус угла x, задаваемого в радианах
# tan(x)	Тангенс угла x, задаваемого в радианах
# acos(x)	Возвращает угол в радианах от 00 до \piπ, cos которого равен x
# asin(x)	Возвращает угол в радианах от -pi/2 до pi/2, sin которого равен х
# atan(x)	Возвращает угол в радианах от -pi/2 до pi/2, tan которого равен х
# atan2(y, x)	Полярный угол (в радианах) точки с координатами (x, y)



# + - * /
# print(5 ** 2)  # степень числа
# print(125 ** (1/3))  # кубический корень
# print(-25 ** (1/2))
# print(pow(5, 2))  # степень числа
# print(pow(-25, 0.5))
# print(2 ** 325)
# print(7 // 3)  # целая часть от деления. РЕЗУЛЬТАТ ДЕЛЕНИЯ ВСЕГДА ФЛОАТ
# print(7 % 3)  # остаток от деления
# print(divmod(7, 3))  # (//, %)
# print(abs(-7))  # модуль числа
# input - ВСЕГДА ВЫВОДИТ СТРОКУ, ПОЭТОМУ В НАЧАЛЕ И ПРИСВАЕМ ТИП ПЕРЕМЕННОЙ ЕСЛИ НУЖНА НЕ СТРОКА
# if условие1:    # если
#     блок кода 1
# elif условие2:  # иначе если
#     блок кода 2
# else:           # иначе при всех остальных условиях
#     блок кода 3

# x = int(input('Введите число: '))
# if x > 0:
#     print('Число положительное.')
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно 0")

# > больше
# < меньше
# >= больше или равно
# <= меньше или равно
# == равно
# != не равно

# Логические операции
# a and b  логическое И, True, если оба равны True
# a or b   логическое ИЛИ, True, если хотя бы один равен  True
# not a    логическое НЕ   not True = False   not False = True

# a, b = -7, (0,)  # обращение по индексу к елементу списка, присваем  значение 0
# # # a, b = b, a
# print(b)
# if a < 0 and b:
#     print('cat')
# exit()
# False = False, 0, None, [], (), {}, ''
# True = True, != 0, len(iterable)>0

# x = input('Какой сегодня день? ')
# if x == 'Суббота' or x == 'Воскресенье':
#     print('Выходной')
# else:
#     print('Рабочий день')

# # Строки str
# контейнер строк '', "", '''hgh''' тройная кавычка сохраняет форматирование текста
# a = 'white cat blACK cat'
# b = 'dog'
# c = 7
# print(a + b + str(c))  # конкатенация(только строки) это- операция склеивания объектов линейной структуры,
# # склеивает без пробелов
# print(a, b, c)   # таким способом выводит любой тип данных
# print(b * 3)  # выводит текст три раза
# print('-' * 80)  # пример
# print('cat' in a)  # проверяет вхождение подстроки в строку(есть ли заданное слово или буква в строке)
# print(len(b))  # длина строки(кол-во символов)
# print(a.count('cat', 5))  # считает количество подстрок в строке(считает заданный елемент в заданном интервале)
# print(a.index('t'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(a.rindex('t'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(a.find('t'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(a.rfind('йййt'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(a.replace('cat', 'cow').replace('black', 'green'))  # замена текста
# print(a.replace('cat', 'cow', 1))  # можно указать количество замен
# print('BMW'.lower())  # перевести строку в нижний регистр
# print('cat'.upper())  # переводит строку в верхний регистр
# print('Apple'.swapcase())  # меняет регистр букв местами
# print(a.title())  # меняет первую букву каждого слова на заглавную, а все остальные на строчные
# print(a.capitalize())  # меняет первую букву строки на заглавную, а все остальные на строчные
#
# a = 'white    cat           black   cat'
# print(a.split(' '))  # разбивает строку на список текстовых элементов по разделителю
# print(a.split())  # по умолчанию разбивает по множественному пробелу
# print(a.split(maxsplit=2))  # можно указать кол-во разбиений
# print(a.split('cat'))
#
# a = 'mytextcatdog'
# print(a.split('t'))
#
# x = ['white', 'cat', 'black', 'cat']
# print('*+-'.join(x))  # склеивает в строку список текстовых элементов

# s = '''white cat
# black cat
# yellow submarine'''
# print(s.splitlines(keepends=True)) # keepends сохраненяет \n  в конце элементов
# x = 'Catland'
# print(x.endswith('land'))
# print(x.endswith(('land2', 'zoom')))
# print(x.endswith('tl', 0, 4))  # проверка заканчивается ли текст на указанные варианты, координаты - это индексы
# print(x.startswith('Cat'))  # проверка начинается ли текст на указанные варианты
# y = 'профессор Иванов П И'
# print(y.rsplit(maxsplit=2))


#
# a = 'apple'
# b = '12'
# c = 'apple 12'
# print(a.isalpha())  # состоит ли только из букв
# print(a.isdigit())  # состоит ли только из цифр
# print(a.isalnum())  # состоит ли только из букв или цифр
# print(a.isspace())  # состоит ли только из пробельных символов (пробел, табуляция \t, перенос строки \n)
# print(a.islower())  # состоит ли строка из строчных букв
# print(a.isupper())  # состоит ли строка из заглавных букв
# print(a.istitle())  # начинаются ли слова в строке с заглавных букв
#
# # fio = input('Введите ваше ФИО: ')
# # if fio.istitle():
# #     print(fio)
# # else:
# #     fio = fio.title()
# #     print(fio)
#
# print(isinstance(a, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# print(type(a))  # показывает тип переменной
# print('***apple******'.strip('*'))  # удаляет с начала и конца строки указанные символы
# print('***apple******'.lstrip('*'))  # удаляет с начала строки указанные символы
# print('***apple******'.rstrip('*'))  # удаляет с конца строки указанные символы
# print('   apple           '.strip())  # по умолчанию удаляет пробельные символы
# print('+-*--+apple+++----***'.strip('+-*'))
# print(ord('?'))  # показывает код символа
# print(chr(43457), 'text', chr(43458))  # показывает символ по коду
#
# for i in range(55296):
#     print(chr(i), end=' ')
#     if i % 50 == 0:
#         print('\n', i, ': ', end='')

# Символы:  https://unicode-table.com/ru/sets/symbols-for-steam/
# s = '''white cat
# black cat
# yellow submarine'''
# print(s.splitlines(keepends=True)) # keepends сохраненяет \n  в конце элементов
# x = 'Catland'
# print(x.endswith('land'))
# print(x.endswith(('land2', 'zoom')))
# print(x.endswith('tl', 0, 4))  # проверка заканчивается ли текст на указанные варианты, координаты - это индексы
# print(x.startswith('Cat'))  # проверка начинается ли текст на указанные варианты
# y = 'профессор Иванов П И'
# print(y.rsplit(maxsplit=2))

# Интервалы, срезы, slices
# a = 'white cat black cat'
# print(a[0])  # первый символ
# print(a[-1])  # последний символ
# print(a[6:9])  # с 6 по 8 символы
# print(a[:5])  # с начала строки по 4 символы
# print(a[16:])  # с 16 до конца строки
# print(a[-3:])  # с -3 до конца строки
# print(a[6:16:2])  # с 6 по 15 с шагом 2
# print(a[:])  # все элементы обьекта
# print(a[::-1])  # развернуть объект
# слайсы можно использовать со след.  типами данных : кортеж, список, строка, словарь

# Тернарный оператор
# if expression:
#     on_true
# else:
#     on_false
#
# on_true if expression else on_false

# x, y = 5, 8
# if x > y:
#     print(x)
# else:
#     print(y)
#
# z = x if x > y else y
# print(z)

# *a, b, c = 5, 7, 6, 7, 8
# print(a, b, c)  # распаковка отдает елементы из итерируемого обьекта
# print(*[1, 2, 3])  # распакует элементы списка, можно применять к любому итерируемому обьекту
#
# # # Списки list
# a = [1, 2, 3, 2, 1]
# b = [5, 6, 7]
# print(a + b) # обьеденение двух списков
# print(b * 3)
# print(a[1:4])
# print(max(a))  # максимальный элемент в списке
# print(max(0 or None or 5, 4)) # сравнивает заданные елементы, если первый елем-т 0, переходит к второму,
# посе сравнивает елементы и выводит мкимальный, можно задавать больше двух елем-тов перечисляя через or
# print(min(b))  # минимальный элемент в списке
# print(sum(b))  # сумма списка
# print(sum(b, 100))  # второй аргумент - первое слагаемое
# x = [[1, 2, 3], [4, 5, 6]]
# # print(sum(x, []))  # преобразовать двумерный список в одномерный
# # print(len(a))
# # print(2 in a)
# # print(a.count(1))  # считает количество 1 в списке а
# # print(a.index(2))  # возвращает индекс вхождения ПЕРВОГО элемента от start до end, если элемента нет "ошибка"
# print(sorted(a, reverse=True))  # возвращает отсортированный список
# print(a)
# a.sort()  # сортирует исходник
# print(a)
# a.reverse()  # разворачивает список
# print(a)
# a.append(4)  # добавляет только один элемент в конец списка
# print(a)
# a.extend(b)  # добавляет элементы списка b в конец списка а(элементов может быть много либо в строке либо в списке))
# print(a)
# a.extend('cat')  # добавляет элементы списка b в конец списка а
# print(a)
# a.insert(2, 8)  # вставляет элемент 8 на индекс 2
# print(a)
# a.remove(2)  # удаляет первый найденный элемент
# print(a)
# # d = a.pop(1)  # удаляет один элемент по индексу и возвращает его d
# # print(a, d)
# # d = a.pop()  # по умолчанию -  удалаяет и выводит последний элемент
# # print(a, d)
# # del a[1]  # удаляет элемент по индексу, del может удалить весь объект
# # print(a)
# # a2 = a.copy()  # копия списка
# # a2.clear()  # очистить список
# # print(a2)
# #
# # a = [1, 2, 3]
# # a2 = a.copy()
# # # a2 = a[:]  # скопировать елементы списка
# # # a2 = a + []  # скопировать елементы списка
# # # a2 = a * 1  # скопировать елементы списка
# # a[0] = 7
# # print(a, a2)
# # print(a == a2)
# #
# # # a = [1, 2, 3]
# # # a.append(a)
# # # print(a)
# # # print(a[3])
#
#
# # a = a + 5 # сокращенная форма присваивания, знак ставим такой как нам нужен
# # a += 5
#
# # egor_pupil  # snike style
# # egorWorkerInItaly  # camel style
#
# # Множества set
# # все елементы уникальны, повторы удаляет, строку разбивает по буквам
# s = [2, 4, 4, 6, 6, 2]
# b = set(s)
# print(b)
# print(set('apple'))
# print(len(b))
# print(2 in b)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {5, 6}
#
# print(b.isdisjoint(c))  # True, если НЕ имеются общие элементы
# print(c.issubset(b))  # c <= b, если b содержит все елементы с то True
# print(c <= b)
# print(b.issuperset(c))  # b >= c
# print(b >= c)
#
# football = {'A', 'B', 'C'}
# chess = {'B', 'C', 'D'}
#
# print(football.union(chess))  # объединение
# print(football | chess)
#
# print(football.intersection(chess))  # пересечение выводит одинаковые елементы
# print(football & chess)
#
# print(football.difference(chess))  # разница выводит елементы которые не совпадают
# print(football - chess)
#
# print(football.symmetric_difference(chess))  # симметричная разница (складываем ножества и удаляем пересечения)
# print(football ^ chess)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# a.intersection_update(b)  # a = a & b    a &= b # выводит пересечение
# print(a)
#
# b.difference_update(a)  # b = b - a    b -= a(убирает елементы из b такие же как есть в а)
# print(b)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# a.symmetric_difference_update(b)  # a = a ^ b    a ^= b  # симметричная разница (складываем ножества и удаляем пересечения)
# print(a)
#
# a.add(8)  # добавляет элемент (неизменяемого типа) в множество(элемент целиком, по символам не разбивает
# a.add('cat')
# a |= {9}
# print(a)
#
# a.update({3, 4})  # объединяет элементы итерируемого объекта с множеством(разбивает по символам)
# a.update('cat')
# print(a)
#
# a.remove(6)  # удаляет элемент множества, если элемента нет - ошибка
# print(a)
# #
# # a.discard(18)  # удаляет элемент множества, если элемента нет - pass
# # print(a)
# #
# # d = a.pop()  # удаляет и возвращает случайный элемент множества.(технически удаляет первый елемент множества)
# # print(a, d)
# #
# # a2 = a.copy()
# # a2.clear()
# #
# # # Тип range
# # print(*range(2, 11, 2))  # целые чётные числа от 2 до 10
# ВСЕ ФУНКЦИИ КОТОРЫЕ В ТЕОРИИ ЗАПИСАНЫ В ПРИНТЕ НЕ РАБОЧИЕ!!!!! ИСХОДНИК НЕ МЕНЯЮТ НЕОБХОДИМО ДЕЛАТЬ ПРИСВОЕНИЕ!!!!!


#
# # Основные способы форматирования строк
# name = 'Alice'
# age = 20
# # 1. Конкатенация
# print('Меня зовут ' + name + ". Мне " + str(age) + ' лет.')
#
# # 2. % форматирование
# print('Меня зовут %s. Мне %d лет.' % (name, age))  # digit - любая цифра(int)
# print('Меня зовут %(x)s. Мне %(y)d лет.' % ({'y': age, 'x': name}))
#
# # 3. Форматирование методом format()
# print('Меня зовут {}. Мне {} лет.'.format(name, age))
# print('Меня зовут {x}. Мне {y} лет.'.format(x=name, y=age))
#
# # 4. f - строки  python >= 3.6
# print(f'Меня зовут {name}. Мне {age} лет.')
# pi = 3.1415926
# print(f'Число pi = {pi:.2f}')  # f - float, работает только с числами, : - форматирование числа, . - после точки оставить два знака
# print(f'pi * age = {pi * age}')
# planets = ['Меркурий', 'Венера', 'Марс']
# print(f'Ближайшая к нам планета {planets[2]}')
# print(f'Ближайшая к нам планета {planets[2].upper()}')
# print(f'Округление 3.5 = {round(3.5)} округление 4.5 = {round(4.5458, 2)}')   # банковское округление,
# округляет к ближайшему четному числу, вторая цифра до скольки цифр округлять
# # в f строке отсутсвует распаковка
#
# print("{1:*^20}".format('Выравнивание', 'cat', 'dog'))   # ноль - это индекс елемента который нам нужно выровнять
# print("{0:>20}".format('Выравнивание'))
# print("{0:*<20}".format('Выравнивание'))
# print()
# print(f'{"Выравнивание":*^20}')
# print(f'{"Выравнивание":*>20}')
# print(f'{"Выравнивание":*<20}')
# z = 1
# d = 20
# print(f'{["Выравнивание", "cat"][z]:*^{d}}')
#
# print('apple'.center(20, '*'))  # возвращает отцентрированную строку по краям которой стоит *
#
# a, b = 5, 7
# print(a, b, end='***')  # end определяет чем заканчивается вывод строки, по умолчанию \n
# print(a, b, sep='+')  # sep определяет, что стоит между переменными, по умолчанию пробел
# print(a, b, a, b, sep='-', end='!!!')
# print('cat')
#
# # print(5.6 // 1)
# # print(-5.6 // 1)
#
# # Словари dict
# a = {'key': 'value', 1: 'cat', 1.0: 'dog', True: 'cow'}  # коллизия хеширования, ключи необходимо задавать учитивая
# # каким будет значение хеш, оно должно быть разным, лучше всего когда все ключи относятся к разным типам данных
# b = {0: 'cat', 0.0: 'dog', False: 'cow'}
# print(a)
# d = {'key': 1, 123: 2, (1, 2): 3}  # безопасные типы данных, в значение ключа можно вкладывать любые данные, еще один
# # слоаарь и т.д
# week = {
#     'Выходной': 'Воскресенье',
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг'
# }
# print(week['Выходной'])  # возвращает значение по ключу, применяем, когда уверены в наличие ключа
# print(week.get(2, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - None или Значение
# которое указали во втором параметре
# print(week.setdefault(5, "Пятница"))  # возвращает значение по ключу, если ключа нет - создаст его
# print(week.keys())  # возвращает все ключи
# print(*week.values(), sep='\n')  # возвращает все значения
# print(*week.items(), sep='\n')  # возвращает (ключ, значение)
# print(week)
# week.update({6: 'Суббота'})  # добавляет элемент(ы) словаря
# week[7] = 'Воскресенье' # добавляет элемент(ы) словаря
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
#
# fruits = ['apple', 'orange', 'grape']
# store = {}.fromkeys(fruits, 0)  # создаёт словарь из итерируемого объекта ключей с одним значением для всех,
# по умолчанию - None
# print(store)
#
# id_users = {
#     12: 'Alex',
#     42: 'Alice',
#     82: 'Bob'
# }
# user = 120
# print(f'Привет {id_users.get(user, "незнакомец")}')
#
# x = {1: 'one', 2: 'two'}
# y = {True: 'cat', False: 'dog'}
# # z = x | y  # python >= 3.9
# z = {**x, **y}  # объединение словарей
# print(z)
#
# # Сортировка словаря по значениям
# store = {'apple': 40, 'orange': 80, 'lemon': 70, 'kiwi': 120}
# print(sorted(store, key=store.get))  # key также используется в min, max

# from pprint import pprint
# pprint(week)

# Цикл for
# for i in iterable:
#     тело цикла
# else:
#     код выполняться, если цикл завершился нормально (без break)

# a = [1, 2, 7, 12, 14, 34, 57]
# for i in a:
#     if i == 12:
#         continue  # досрочное завершение итерации
#     if i == 60:
#         break  # досрочное завершение цикла
#     print(i)
# else:
#     print('cat')

# print(*range(2, 7, 2))

# for i in 'dog':
#     print('cat')
#
# for x in range(2, 11, 2):
#     print(x)

# for i in enumerate('apple', 10):  # enumerate возвращает (индекс, элемент), можно задать с какого числа начинать индексацию
#     print(i)

# for ind, elem in enumerate('apple', 1):
#     print(ind * elem)
#
# for x, y, z in [[1, 2, 3], [4, 5, 6]]:
#     print(x * y * z)

# print(*enumerate('apple', 1))

# Списковые включение list comprehension ("Генератор списков")
# s = []
# for i in range(1, 11):
#     s.append(i ** 2)
# print(s)
#
# s = [i ** 2 for i in range(1, 11)]  # итераторное выражение
# s0 = {i ** 2 for i in range(1, 11)}
# s1 = {i: i ** 2 for i in range(1, 11)}
# print(s)
# print(s1)
#
# s = [i ** 2 for i in range(1, 11) if i % 2 == 0]  # if только один
# print(s)
#
# # Вывести чётные числа в интервале [1, 20], если число меньше или равно 10, то - квадрат, а если больше 10 - куб.
# s = [i ** 2 if i <= 10 else i ** 3 for i in range(1, 21) if i % 2 == 0]
# print(s)
# s = [(i ** 2 if i < 5 else -i ** 2) if i <= 10 else i ** 3 for i in range(1, 21) if i % 2 == 0]
# print(s)

# for x in range(10):
#     for y in range(10):
#         if (x * 10 + y) % 2 == 0:
#             print(x * 10 + y)
# #         print(f'x = {x}   y = {y}   {x * 10 + y}')
#
# print([x * 10 + y for x in range(10) for y in range(10) if (x * 10 + y) % 2 == 0])


# for i in 'cat':
#     for x in [1, 2, 3]:
#         print(i * x)

# print([i * x for i in 'cat' for x in [1, 2, 3]])
# print([i * x for i in 'cat' for x in [1, 2, 3] if len(i * x) == 2])

# Сгенерировать список из букв имён меньших 4 символов
# names = ['Jerry', 'Tom', 'Jack', 'Yang', 'Bob']
# b = []
# for i in names:
#     for a in i:
#         if len(i) < 4:
#             b.append(a)
# print(b)

# b = []
# for i in names:
#     if len(i) < 4:
#         for a in i:
#             b.append(a)
# print(b)

# for _ in range(6):  # если не используем переменную можем использовать просто нижнее подчеркивание
# print(a.pop())

# РАЗОБРАТЬСЯ КАК РАБОТАЕТ ВЛОЖЕНЫЙ ЦИКЛ, ПОПРОБОВАТЬ ЗАПИСАТЬ ЕГО В ОДНУ СТРОКУ
# b = [a for i in names for a in i if len(i) < 4]
# print(b)
# print([a for i in names if len(i) < 4 for a in i])

# a = [i ** 2 for i in range(5_000_000)]
# a2 = (i ** 2 for i in range(5_000_000))
# print(a.__sizeof__())
# print(a2.__sizeof__())

# print(next(a2))  # берём с итератора элемент

# Цикл while
# while условие:
#     тело цикла
# else:
#     код выполняется, если цикл закончился не по break

# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#     if i == 6:
#         break
#     print(i)
# else:
#     print('cat')

# while True:
#     x = input('Введите число: ')
#     if x == 'exit':
#         break
#     print(int(x) ** 2)


# n = 6
# for i in range(2, n + 1):
#     print(i, '-', *[j for j in range(1, i) if i % j == 0])

# Многомерные массивы (списки)

# a = [1, 2, 3]
# b = [[1, 2, 3], [1, 2, 3]]
# c = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [1, 2, 3]]]
# print(a[1])
# print(b[0][2])
# print(c[1][0][2])
# a = [0] * 10
# print(a)
# b = [[0] * 10 for i in range(2)]
# b[0][0] = 7
# print(b)
# d = [ [[0] * 5 for i in range(2)] for _ in range(3)]
# print(d)

# Распаковка двумерного в одномерный
# a = [[1, 5, 7], [2, 4, 8]]
# print(sum(a, []))
#
# b = []
# for i in a:
#     b += i
# print(b)
#
# print([j for i in a for j in i])

# Функция
# DRY don't repeat youself
# между функциями одна пустая строка, между выводом две
# def my_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def super_sum(*x):
#     return sum(x)
#
# def cats(x):
#     print('cat' * x)
#
#
# print(my_max(5, 7))
# print(super_sum(5, 6, 7, 8))
# cats(5)
# cats(10)

# a, b, *c = 1, 2, 3, 4, 5

# Основы криптографии
# x = 'abcde'
# y = '12345'
# s = 'bacdecbb'
# z = str.maketrans(x, y)
# print(s.translate(z))

# def f(a, b, *x):    # если нужно вывести n - кол-во переменных применяем распаковку,
#     print(a, b, x)  # при рапаковке в параметрах функии применяем ее только последним аргументом если неименованные,
#     выводит кортеж
#
#
# f(7, 8, 9, 5, 6)

# def func(name, *mark, math, phizika):  # именованные аргументы всегда пишем последними
#     print(name, ':', *mark)
#     print(math, phizika)

# def func2(name, *mark, **pred):  # именованные аргументы всегда пишем последними
#     print(name, ':', *mark)
#     # print(pred)
#     print(*[f'{i} - {pred[i]}' for i in pred], sep='\n')
#     print('Ему в музыканты!' if 'music' in pred else 'Скрипку не давать!')
    #     print('Ему в музыканты!')
    # else:
    #     print('Скрипку не давать!')


# func('Alex', 20, 30, math=5, phizika=4)
# func2('Alex', 20, 30, math=5, phizika=4, him=5)

# лямда функция и пространство имен
# Лямда функция - безимянная функция
# def func(x):
#     return x[1]


# students = [
#     ('ALice', 8),
#     ('Alex', 6),
#     ('Dasha', 10)
# ]
#
# print(sorted(students, key=lambda x: x[1])) # х это параметр(в примере это кортеж), после : записываем то что в return
# меняем критерий сортитовки, в кеу обязательно должна указываться функция
# z = lambda x : len(x) * x  # лямду можно присвоить переменной
# print(z('cat'))
# print(z('apple'))
#
# grades = [
#     {'name': 'Alice', 'final': 95},
#     {'name': 'Alex', 'final': 100},
#     {'name': 'Bob', 'final': 80}
# ]
# print(sorted(grades, key=lambda x: x['final']))  # в этом примере х - словарь
# print(sorted(grades, key=lambda x: x['name'], reverse=True))

# Область видимости переменных в функции
# def func():  # каждая функция имеет свое локальное пространство имен, т.е это отдельный обьект
#
#     def func2():    #  в функции могут хранится переменые, функции и т.д если дочерней функии не задана переменная,
#         print(x)    #  она будет искать переменную на уровень выше
#
#     x = 15
#     func2()
#     print(x)
#
#
# x = 10
# func()
# print(x)

# ---------

# def func():  # каждая функция имеет свое локальное пространство имен, т.е это отдельный обьект
#     global x  # эта переменная становится глобальной, мы меняем либо используем ее значение
#     print(x)
#     x = 15
#     print(x)
#
#
# x = 10
# func()
# print(x)

# ---------

# def func():
#
#     def func2():
#         global x
#         x = 100
#         print(x)
#
#     x = 15
#     func2()
#     print(x)
#
#
# x = 10
# func()
# print(x)

# -----

# def func():
#
#     def func2():
#         nonlocal x  # смотрит на уровень выше только в локальное простаранство имён родительской функции.
#         x += 100    # меняет значение родительской переменной
#         print(x)
#
#     # global x # в этом случае не будет х в локальном пространстве имен
#     x = 15
#     func2()
#     print(x)
#
#
# x = 10
# func()
# print(x)

# ------------

# def func(x): # изменяемые типы данных передают в функию ССЫЛКУ!!!
#     x[0] = 5
#     print(x)
#
#
# x = [1, 2, 3]
# func(x)
# print(x)

# ----


# def func(x):
#
#     def func2(x):
#         x[1] = 7
#         print(x)
#
#     x = [10, 20, 30]
#     func2(x)
#     print(x)
#
#
# x = [1, 2, 3]
# func(x)
# print(x)

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

# q = ask_ok('Хотите выйти из программы? ')
# q = ask_ok('Хотите выйти из программы? ', 2)
# q = ask_ok('Хотите выйти из программы? ', 4, 'Ответ должен быть yes или no!')
# if q:
#     print('Выходим из программы')
# else:
#     print('Остаёмся в программе')

# import my_functions # импортируем файл с функциями
# from my_functions import super_sum  # если нужно импортировать только одну конкретную функцию
# from my_functions import super_sum as sm #  если нужно сократить название функции


# print(my_functions.super_sum(1, 2, 3, 4, 5))
# print(super_sum(1, 2, 3, 4, 5))
# print(sm(1, 2, 3, 4, 5))


# ФВП, бработка ошибок
# map(function, iterables)  возвращает последовательность, полученную применение function к элементам iterables(map это итератор)
# map(func, iterable) = func(i) for i in iterable

# список квадратов от 1 до 10
# a = []
# for i in range(1, 11):
#     a.append(i ** 2)
# print(a)

# print([i ** 2 for i in range(1, 11)])

# def func(x):
#     return x ** 2
#
# print(list(map(func, range(1, 11))))

# print(list(map(lambda x: x ** 2, range(1, 11))))

# number = 123456
# b = 0
# for i in str(number):
#     b += int(i)
# print(b)

# def sum_1(x):
#     return int(x)
#
# number = 7123456
# print(sum(map(sum_1, str(number))))

# number = 7123456
# print(sum(map(lambda x: int(x), str(number))))
# print(sum(map(int, str(number))))

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# print(list(map(lambda x, y: x * y, list1, list2)))

# list1 = [1, 2, 3, 4]
# list2 = 'cats'
# print(list(map(lambda x, y: x * y, list1, list2)))

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8]
# list3 = [5, 6] # если в мап передать обьекты разной длинны, будет итерироваться по меньшему обьекту(лишний елемент отбросит) похожа на zip
# print(list(map(lambda x, y, z: x * y  * z, list1, list2, list3)))

# filter(function, iterable)  возвращает последовательность, состоящую из тех элементов последовательности iterable для которых function является истиной
# filter(function, iterable) = i for i in iterable if func(i)

# def func(x):
#     return x % 2 == 0
#
# print(list(filter(func, range(11))))

# Вывести список простых чисел в интервале от 2 до 100 используя filter

# def func(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# print(list(filter(func, range(2, 100))))

# 100 - 10 ** 2 = 100
# 2 4 5 10 - 10 20 25 50  100

# zip(sequence) функция объединяет последовательность разной длины в итератор zip кортежей
# a = (1, 2, 3, 4)
# b = 'cats'
# print(*zip(a, b))

# from itertools import zip_longest
# Создадим словарь из двух списков
# products = ['butter', 'bread', 'milk', 'apple', 'kiwi']
# prices = [10, 50, 35, 25]
# print(dict(zip(products, prices)))
# print(dict(zip_longest(products, prices, fillvalue=0)))

# Распакуем списко кортежей в 2 кортежа
# s = [('butter', 10), ('bread', 50), ('milk', 35), ('apple', 25)]
# products, prices = zip(*s)
# print(products, prices)

# Какие високосные годы, начиная с 1582 года до 2017, имели сумму цифр, равную 9?
# Високосный год — год, который делится на 4, но при этом не делится на 100 либо делится на 400.


# a = filter(lambda x: (x % 4 == 0 and x % 100) or x % 400 == 0, range(1582, 2017))
#
# print(*filter(lambda x: sum(map(int, str(x))) == 9, a))

# Функции all() / any()
# keys_base = ['title', 'id', 'description', 'data']
# date = [
#     {
#         'title': 'titel1',
#         'id': 'id1',
#         'description': 'description1',
#         'data': 'data1'
#     },
#     {
#         'title': 'titel2',
#         'id': 'id2',
#         'description': 'description2',
#         'data': 'data2'
#     }
# ]
# for d in date:
#     for key in keys_base:
#         if key not in d.keys():
#             print('Ключа не  хватает!')

# for d in date:
#     if not all([key in d.keys() for key in keys_base]):
#         print('Ключа не  хватает!')

# all() идёт по списку True/False (выражения, которые сводятся к этим значениям) и прекращает проверку после первого False
# all() будет равен True, если все элементы списка равны True или список пустой
# any() будет равен True, если хоят бы 1 элемент равен True

# x = [True, True, False]
# if any(x):
#     print('Как минимум 1 True')
# if all(x):
#     print('Все элементы True или нет ни одного False')
# if any(x) and not all(x):
#     print('Как минимум 1 True и как минимум 1 False')
#
# print(all([0, 2, 3]))

# numbers = [5, 10, 100, 1000]
# if [i for i in numbers if i < 10]:
#     print('В списке есть числа меньше 10')
#
# if any(i < 10 for i in numbers):
#     print('В списке есть числа меньше 10')



# Рекурсия
# 5! = 1 * 2 * 3 * 4 * 5 факториал
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def factorial(n):
#     return n * factorial(n - 1) if n == 1 else 1
#
# print(factorial(5))
# 5 * (4 * (3 * (2 * 1))
# f(5) -> f(4) -> f(3) -> f(2) -> f(1)
# def color(start, sp):
#     if not sp:
#         print(start)
#     for i, y in enumerate(sp):
#         color(start + [y], sp[: i] + sp[i + 1:])
#
#
# color([], ['R', 'G', 'B'])  #алгоритм разделения, в правой части буду обработанные ел-ты, в левой те которые нужно обработать

# Обработка исключений

# работа с файлами

# Файлы:
# f1 = open('my_functions.py', 'r', encoding='UTF-8')
# f2 = open('my_functions2.py', 'w', encoding='UTF-8')  # C:\имя можно указать путь файла куда нужно записать
# for line in f1.readlines():
#     f2.write(line)
# f2.close()
# f1.close()

# with open('my_functions.py', 'r', encoding='UTF-8') as f10:
#     with open('my_functions3.py', 'w', encoding='UTF-8') as f20:
#         for line in f10.readlines():
#             f20.write(line)

# Список режимов доступа к файлам:

# r открывает файл только для чтения, указатель стоит в начале файла, только текстовые
# rb тоже для бинарного файла, в бинарном файле могут быть любые символы, не только текст(картинки, музыка, видео, то что сжато), если файл нужно сохранить в пдф, мп3, мп4 и т.д.
# r+ открывает файл для чтения и записи, указатель стоит в начале файла, только текстовые
# rb+ тоже для бинарного файла
# если есть буква b файл бинарный

# w открывает файл только для записи, указатель стоит в начале файла, создаст файл, если его нет
# wb тоже для бинарного файла
# w+ открывает файл для чтения и записи, указатель стоит в начале файла, создаст файл, если его нет
# wb+ тоже для бинарного файла

# a открывает файл для добавления информации, указатель стоит в конце файла, создаст файл, если его нет
# ab тоже для бинарного файла
# a+ открывает файл для чтения и добавления информации, указатель стоит в конце файла, создаст файл, если его нет
# ab+ тоже для бинарного файла

# x открывает файл только для записи, указатель стоит в начале файла, если файла нет - выдаст ошибку
# f обращение к обьекту файла
# f.read(size) функция читает некоторое количество данных и возвращает её в виде строки, size - не обязательный числовой аргумент, если он опущен, то возвратит всё содержимое файла
# f.readline() читает текущую строку из файла там где стоит курсор
# f.readlines() возвращает содержимое файла списком строк
# f.write(s)  записывает содержимое строки s в файл там где стоит курсор
# f.writelines(sp) записывает всё содержимое sp в файл списком строк

# f.seek(Смещение, Откуда) изменяет позицию курсора.
# Позиция вычисляется прибавлением Смещения к точке отсчёта.
# Точка отсчёта выбирается из параметра Откуда:
# 0 - то отмеряется смещение от начала файла (по умолчанию)
# 1 - то отмеряется от текущей позиции файла
# 2 - то отмеряется от конца файла, смещение указываем отрицательное

# f.tell() возвращает число, представляющее собой текущую позицию в файле(где стоит курсор)
# f.close() закрывает файл, если работать с with не нужен
# создаем файл, w метод что мы делаем с файлом
# with open('fruits.txt', 'w', encoding='UTF-8') as f:  # as f указываем сокращенное имя файла как будем обращаться к нему дальше
#     while True:
#         a = input('Введите фрукт и количество через пробел: ')
#         if a == 'exit':
#             break
#         f.write(a + '\n')
# считываем созданный файл для работы с ним r
# with open('fruits.txt', 'r', encoding='UTF-8') as f:
    # print(f.readlines())
    # d = {}
    # for line in f.readlines():
    #     fruit, num = line.split()
        # наполняем словарь
        # if fruit in d.keys():
        #     d[fruit] += int(num)
        # else:
        #     d[fruit] = int(num)
#         d[fruit] = d.setdefault(fruit, 0) + int(num)
#
# for x, y in d.items():
#     print(f'{x} -> {y}')

# Копируем и сохраняем файл из интернета.
# import  requests
#
# url = 'https://static3.depositphotos.com/1000575/154/i/950/depositphotos_1549339-stock-photo-lithuania-landscape-panorama.jpg'
# a = requests.get(url)
# with open('picture.jpg', 'wb') as f:
#     f.write(a.content)

# CSV файлы хранят информацию в табличном формате
# f.writerow(s) записывает обьект s в файл f
# f.writerows(s) записывает итерируемый обьект s в файл f
# csv.writer создаем обьект который записывает данные в cvs файлы по каким-то параметрам
# delimiter - разделитель, то чем будут оазделяться элементы
# quoting=csv.QUOTE_ALL помещает значения в кавычки
# newline='' пишим стандартно не меняя
# csv.reader(f) создает обьект который будет читать наш файл
# csv.DictWriter если нужно записать словарь
# fieldnames= параметр при создании словарей в который передаем название колонок
# csv.DictReader(f) создает обьект который будет читать наш файл для словарей
# import csv
# data = [
#     ['Tom', 28],
#     ['Jerry', 20],
#     ['Alice', 25]
# ]
# path = 'names.csv'

# with open(path, 'w', newline='') as f:
#     my_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)  # quoting-помещает значения в кавычки
#     # my_writer.writerows(data)
#     for i in data:
#         my_writer.writerow(i)

# with open(path) as f:  # открываем файл для чтения, открывает по умолчанию 'r' можно не прописывать
#     my_reader = csv.reader(f)
#     for i, j in my_reader:
#         print(f'{i} -> {j}')

# user = ('Cat', 20)
#
# with open(path, 'a', newline='') as f: # добавляем в файл запись
#     my_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)  # помещает значения в кавычки
#     my_writer.writerow(user)

# filename = 'dicts.csv'
# users = [
#     {'name': 'Tom', 'age': 27},
#     {'name': 'Alice', 'age': 35},
#     {'name': 'Jerry', 'age': 17},
# ]
# with open(filename, 'w', newline='') as f:
#     columns = ['name', 'age']  # название колонок
#     my_writer = csv.DictWriter(f, fieldnames=columns)
#     my_writer.writeheader()  # записываем в файл название колонок
#     my_writer.writerows(users)
# # добавляем новый обьект пока файл не закрыт
#     user = {'name': 'Alex', 'age': 25}
#     my_writer.writerow(user)
# # открываем файл для чтения
# with open(filename, 'r', newline='') as f:
#     my_reader = csv.DictReader(f)
#     for i in my_reader:
#         print(i)

# data = [
#     'first_name:last_name:city',
#     'Ivan:Ivanov:Moskva',
#     'James:Bond:London',
#     'Bill:Gats:Orlean'
# ]
# with open('names_city.csv', 'w', newline='') as f:
#     head = data[0].split(':') # название колонок
#     my_writer = csv.DictWriter(f, fieldnames=head) #создаем словарь
#     my_writer.writeheader()  # записываем в файл название колонок
#     for i in data[1:]:
#         user = i.split(':')
#         print(user)
#         # my_writer.writerow(dict(zip(head, user)))
#         print(dict(zip(head, user)))

# data = ["first_name,last_name,city".split(","),
#         "Tyrese,Hirthe,Strackeport".split(","),
#         "Jules,Dicki,Lake Nickolasville".split(","),
#         "Dedric,Medhurst,Stiedemannberg".split(",")
#         ]
# with open('book1.csv', 'w', newline='') as b:
#     head = data[0]
#     my_file = csv.DictWriter(b, fieldnames=head)
#     my_file.writeheader()
#     for i in data[1:]:
#         my_file.writerow(dict(zip(head, i)))
#         # print(dict(zip(head,i)))
#
# with open('book1.csv') as b:
#     my_file = csv.DictReader(b)
#     for i in my_file:
#         print(f"{i['first_name']} {i['last_name']}: {i['city']}")
        # print(' - '.join(i.values()))


# import json

# 1) ключ только str
# 2) false, true в json с маленькой буквы
# 3) null это None
# 4) строки внутри только в двойных кавычках

# d = {'a': [1, 2, 3], 'b': 12345, 'c': True, 123: None}
# s = json.dumps(d, indent=1)  # преобразует словарь в json-строку, indent=1 - параметр с помощью которого можно задать отступы
# print(s)
# s2 = json.loads(s)  # преобразует json-строку в словарь
# print(s2)

# json.dump(s, file)  # записывает объект json s в файл file
# s3 = json.load(file)  # загуржает json из файла file

# repr()  преобразует словарь в строку
# eval()  преобразует строку в словарь

# d2 = repr(d)
# print(d2, type(d2))
#
# d3 = eval(d2)
# print(d3, type(d3))

# x = '[{"name": "B", "parents": ["A", "C"]}, {"name": "A", "parents": []}, {"name": "C", "parents": ["A"]}]'
# x2 = json.loads(x)
# print(x2, type(x2))


# matplotlib
# re
# как работать с Exсel
# ITERTOOLS
# рекурсия