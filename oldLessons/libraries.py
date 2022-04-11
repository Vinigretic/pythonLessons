import string
# a = string.ascii_letters
# print(a)
# print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)  # 0123456789
# print(string.hexdigits)  # 0123456789abcdefABCDEF
# print(string.octdigits)  # 01234567
# print(string.whitespace)  # пробельные символы
# print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.printable)  # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# s = 'white?, cat: black... cat!'
# print(*map(lambda x: x.strip(string.punctuation), s.split()))
# for i in string.punctuation:
#     s = s.replace(i, '')
# print(s)

# import random
#
# # random.randint(a, b)  случайное целое в интервале [a, b]
# print(random.randint(2, 5))
#
# # random.randrange(2, 10, 2)  случайное целое из последовательности
# print(random.randrange(2, 11, 2))
#
# # random.uniform(2, 5)  случайное дробное от 2 до 5
# print(random.uniform(2, 5))
#
# fruits = ['apple', 'kiwi', 'orange', 'banana']
#
# # random.choice(fruits) случайный элемент НЕ ПУСТОЙ последовательности
# print(random.choice(fruits))
#
# # random.choices(fruits, k=3) возвращает k случайных элементов с возможными повторами
# print(random.choices(fruits, k=3))
#
# # random.sample(fruits, 3)  возвращает несколько случайных элементов БЕЗ повторов
# print(random.sample(fruits, 3))
#
# print(fruits)
# random.shuffle(fruits)  # перемешивает элементы
# print(fruits)

# Системы счисления
# print(bin(19))  # двоичная, 0b при вывводе числа обозначение двоичной системы
# print(oct(19))  # восьмиричная, 0о при вывводе числа обозначение восьмиричной системы
# print(hex(29))  # шестнадцатиричная, 0x при вывводе числа обозначение шестнадцатиричной системы
# print(int('0x1d', 16))  # преобразует из 16 в 10
# print(int('0x1d', 0))  # автоопределение системы счисления

# import time
#
# start = time.time()  # текущее время в секундах с начала цифровой эры
# for i in range(1_000_000):
#     x = i ** 3
# end = time.time() # текущее время окончания работы программы
# print(end - start)

# print(time.ctime(end))  # Mon Jan 24 21:04:41 2022
# time.sleep(3)  # остановка программы в секундах
# print(time.ctime())  # показывает текущую дату-время

# print(time.localtime())  # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=24, tm_hour=21, tm_min=9, tm_sec=18, tm_wday=0, tm_yday=24, tm_isdst=0)
# print(time.localtime().tm_year)
# print(time.strftime('Today is %B %d, %Y.', time.localtime()))
# print(time.monotonic())  # таймер независимый от внешних условий (время с запуска программы) в секундах

# seconds = 123123123
# t = time.localtime(seconds)
# print(t)
# s = time.mktime(t)  # переводит в секунды struct_time
# print(s)

# print(time.timezone)  # смещение местного часового пояса в секундах  (-7200)
# print(time.tzname)  # кортеж их двух строк (имя часового пояса, имя местного часовго пояса) ('Финляндия (зима)', 'Финляндия (лето)')

# a = time.ctime(time.time())
# print(a)
#
# from time import time, ctime
# t = time()
# t = ctime(t)
# f = open("time.txt","w+")
# f.write(t)
# f.close()
# # Later...
# f = open("time.txt", "r")
# print(f)
# f.close()

# Модуль datetime
# from datetime import date, time, datetime, timedelta

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
#
# print(datetime.now())  # 2022-01-28 21:18:27.329330
# print(datetime.now().time())  # 21:18:27.329330
# print(datetime.now().date())  # 2022-01-28
#
# my_date = date(2022, 1, 28)
# print(my_date)  # 2022-01-28
# print(date.today())  # 2022-01-28
# print(date.today().weekday())  # 4

# my_time = time(21, 23, 40)
# print(my_time)  # 21:23:40

# my_datetime = datetime(2022, 1, 28, 22, 12, 43)
# # print(my_datetime)  # 2022-01-28 22:12:43
# # my_datetime2 = datetime.combine(my_date, my_time)
# # print(my_datetime2)  # 2022-01-28 21:23:40
# # print(my_datetime2.year)  # 2022
# print(my_datetime.date)
#
# delta_time1 = timedelta(weeks=2, seconds=20)
# print(delta_time1)  # 14 days, 0:00:20
# print(delta_time1.days)  # 14
# print(delta_time1.total_seconds())  # 1209620.0
# delta_time2 = timedelta(weeks=-4, seconds=-40)
# print(delta_time2)
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
#
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
# print(date.today().strftime('%B'))  # January
#
# # timedelta одна из функций
# # timedelta.total_seconds() переводит разницу времени в секунды
# a = datetime(2015, 1, 12, 10, 0 , 0)
# b = datetime(2015, 1, 12, 10, 10 , 10)
# print(int((b - a).total_seconds()))
# # передача кортежа в datetime с помощью распаковки
# a = (1982, 4, 19)
# print(datetime(*a))
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

# Комбинаторные функции itertools
from itertools import * # импортирует все модули
from itertools import combinations, combinations_with_replacement, product, permutations, cycle, repeat, accumulate, chain, dropwhile, takewhile

# print(*product([0, 1, 2], repeat=2))  # (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) (2, 1) (2, 2)
#
# print(*product('abc', 'abc'))  # ('a', 'a') ('a', 'b') ('a', 'c') ('b', 'a') ('b', 'b') ('b', 'c') ('c', 'a') ('c', 'b') ('c', 'c')
# print(*combinations('abc', 2))  # ('a', 'b') ('a', 'c') ('b', 'c')
# print(*combinations_with_replacement('abc', 2))  # ('a', 'a') ('a', 'b') ('a', 'c') ('b', 'b') ('b', 'c') ('c', 'c')
# print(*combinations_with_replacement([2, 3, 5], 3))  # (2, 2, 2) (2, 2, 3) (2, 2, 5) (2, 3, 3) (2, 3, 5) (2, 5, 5) (3, 3, 3) (3, 3, 5) (3, 5, 5) (5, 5, 5)
# print(*permutations('abc', 2))  # ('a', 'b') ('a', 'c') ('b', 'a') ('b', 'c') ('c', 'a') ('c', 'b')

# a = ['cat', 'dog', 'cow']
# itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз.
# for i in cycle(a):
#     print(i)

# itertools.repeat(elem, n) - повторяет elem n раз.
# for i in repeat(a, 3):
#     print(i)

# b = [1, 2, 3, 4]
# itertools.accumulate(iterable) - аккумулирует суммы.
# print(*accumulate(b))

# c = [5, 6, 7, 8]
# itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор, пока итераторы не кончатся.(складывает итераторы в один)
# print(*chain(b, c))

# itertools.dropwhile(func, iterable) - элементы iterable, начиная с первого, для которого func вернула ложь.
# print(*dropwhile(lambda x: x < 5, [1,4,6,4,1]))

# itertools.takewhile(func, iterable) - элементы до тех пор, пока func возвращает истину.
# print(*takewhile(lambda x: x < 5, [1,4,6,4,1]))  #  --> 1 4

# from itertools import groupby, islice, starmap
# things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
# for  x, y in groupby(things, lambda x: x[0]):
#     print(x, *y)
# print({x: next(y) for  x, y in groupby(things, lambda x: x[1]+x[0])})
# print({x: tuple(*y) for  x, y in groupby(things, lambda x: x[1]+x[0])})

# itertools.islice(iterable[, start], stop[, step]) - итератор, состоящий из среза.
# x = (i for i in range(2, 8))
# print(*islice(x, 2, 4)) # указываем индексы нужного слайса

# itertools.starmap(function, iterable) - применяет функцию к каждому элементу последовательности (каждый элемент распаковывается).
# print(*starmap(pow, [(2,5), (3,2), (10,3)]))  # -> 32 9 1000
# print(*starmap(lambda x,y: x * y, [(2,5), (3,2), (3,10)]))

# Регулярные выражения Regexp/Regex
# Применяется для парсинга и поиска в тексе
import re
print(r'\p{5}')



