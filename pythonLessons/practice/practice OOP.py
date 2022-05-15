# Представьте себе на секунду, что вы Бог и только что сотворили Человека. Люди - это вид, называемый Homo Sapiens,
# и они (обычно) имеют 2 ноги и 2 руки. Создайте атрибуты species, n_legs и n_arms для вашего класса Human.

# class Human:  # создали класс
#     species = 'Homo Sapiens'  # создали атрибуты класса
#     n_arms = 2  # создали атрибуты класса
#     n_legs = 2  # создали атрибуты класса
#
#
# print(Human)  # Печатаем  класс
# print(Human.species)  # печатаем атрибуты класса
# print(Human.n_arms)
# print(Human.n_legs)

# Создайте класс Book, в котором будут атрибуты name и author, со значениями из input. Затем выведите значения.
#
# Input  и Output должны быть в следующем формате:

# Преступление и наказание
# Федор Михайлович Достоевский
# Страх и Трепет
# Сёрен Кьеркегор
# Голова профессора Доуэля
# Александр Романович Беляев

# Вывод

# Преступление и наказание - Федор Михайлович Достоевский
# Страх и Трепет - Сёрен Кьеркегор
# Голова профессора Доуэля - Александр Романович Беляев

# class Book:
#
#     all_books = []
#
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#         Book.all_books.append(self)
#
# book1 = Book(input(''), input(''))
# book2 = Book(input(''), input(''))
# book3 = Book(input(''), input(''))
#
# for i in Book.all_books:
#     print(f'{i.name} - {i.author}')
#
# Создайте класс Movie и определите конструктор класса с такими параметрами, как заголовок, режиссер и год выпуска.
# Затем создайте такие объекты, как «Титаник» (реж. Джеймс Кэмерон, 1997), «Звездные войны» (реж. Джордж Лукас, 1977) и
# «Бойцовский клуб» (реж. Дэвид Финчер, 1999).
#
# Некоторые атрибуты этих объектов будут напечатаны, чтобы проверить их.
#
# Год передается в виде строки.

# class Movie:
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year
#
#
# titanic = Movie('Титаник', 'Джеймс Кэмерон', '1997')
# star_wars = Movie('Звездные войны', 'Джордж Лукас', '1977')
# fight_club = Movie('Бойцовский клуб', 'Дэвид Финчер', '1999')
#
# print(titanic.title)
# print(star_wars.year)
# print(fight_club.director)

# Джон работает в университете. Ему постоянно приходится иметь дело с большим объемом информации об учебном процессе и учениках,
# и поэтому он решил создать программу, которая поможет ему в этом.
# Он разработал систему для создания идентификатора для каждого студента: первая буква имени, фамилия, а затем год рождения.
# Например, идентификатор для Джейдена Смита (р. 1998) будет выглядеть как JSmith1998.
# Джону нужна помощь, чтобы завершить код для удостоверения личности и затем применить его к студентам.
# Создайте идентификатор атрибута экземпляра в методе __init__, рассчитайте его, а затем напечатайте его значение для учащегося.
# Формат ввода:
# Информация об ученике: первая строка имеет имя, вторая - фамилию, а третья - год рождения.
# Формат вывода:
# Идентификатор студента.
# Hint: считать несколько строк из стандартного ввода можно вызвав input() несколько раз.
# Sample Input:
#  Daniel
# Smith
# 1993
# Sample Output:
#  DSmith1993

# class Student:
#
#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         # calculate the id here
#
#     def display_info(self):
#         print(f'{self.name[0]}{self.last_name}{self.birth_year}')
#
#
#
# object1 = Student(input(), input(), input())
# object1.display_info()


# class Ship:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#             # the old sail method that you need to rewrite
#     def sail(self, country):
#         self.country = country
#         print(f'The {self.name} has sailed for {self.country}!')
#
#
#
# black_pearl = Ship("Black Pearl", 'Argentina')
# black_pearl.sail(input())

# Реализуйте класс PiggyBank, который представляет собой олдскульную копилку в форме свиньи. Он имеет два атрибута,
# доллары (dollars) и центы (cents), и их начальные значения передаются в конструктор.
# Создайте метод add_money с двумя параметрами deposit_dollars и deposit_cents, который увеличивает сумму денег в
# копилке. Например, если вы положили в копилку меньше доллара, значение deposit_dollars равно 0.
# Метод не должен ничего печатать!
# Параметры deposit_dollars и deposit_cents метода add_money могут иметь любое значение, но значение центов в
# копилке после добавления не может превышать 99! Если значение deposit_cents после добавления больше 99, вам
# необходимо обновить как значение в долларах, так и значение в центах!
# Подсказка: вы можете использовать оператор целочисленного деления и деления с остатком!

# class PiggyBank:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#     def add_money(self, deposit_dollars, deposit_cents):
#         # self.deposit_dollars = deposit_dollars # в обычных методах атрибуты описывать не нужно
#         # self.deposit_cents = deposit_cents
#         self.dollars = self.dollars + deposit_dollars
#         self.cents = self.cents + deposit_cents
#         if self.cents >= 100:
#             self.dollars = self.dollars + self.cents // 100
#             self.cents = round(self.cents - self.cents // 100 * 100, 2)
#             return self.dollars, self.cents
#
#     def display(self):
#         print(self.dollars, self.cents)
#
# object1 = PiggyBank(10, 90)
# object1.add_money(0, 300)
# object1.display()








