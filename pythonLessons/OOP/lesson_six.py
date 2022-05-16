# Атрибуты класса используются когда нужно определить общее поведение для всех обьектов класса

# class Person:
#     type = 'Person'  # атрибуты класса, доступны всем обьектам класса
#     description = 'decribes a person'
#
# print(Person.type)
# print(Person.description)
#
# Person.type = 'animal'
# print(Person.type)

# class Person:
#     default_name = 'undefined'
#
#     def __init__(self, name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name
#
# object1 = Person('Lina')
# object2 = Person('')
# print(object1.name)
# print(object2.name)

# class Person:
#     name = 'undefined' # атрибут класса
#
#     def print_name(self): # атрибут обьекта, не задан в данном коде и при вызове метода ему будет присвоено значение атрибута
#                           # класса с таким же именем
#         print(self.name)
#
#
# object1 = Person()
# object2 = Person()
# object1.print_name()
# object2.print_name()
#
# object1.name = 'Lina'
# object1.print_name()
# object2.print_name()

# Статические методы - определяют поведение которое не зависит от конкретного обьекта(не принимают ссылку self на обьект)

# class Person:
#     __type = 'Person' # приватный атрибут класса изменять нельзя
#
#     @staticmethod
#     def print_type():
#         print(Person.__type)
#
# Person.print_type()
# object1 = Person()
# object1.print_type()
# Person.__type = 'jdfjdk'
# Person.print_type()

# Все классы в Python имеют общий суперкласс object
# class Person(object): = class Person:
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f'Name: {self.name}, age: {self.age}')
#
# object1 = Person('Vita', 45)
# print(object1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.__str__())


    def __str__(self): # отвечает за представление обьекта, всегда возвращает строку
        return f'Name: {self.name}, age: {self.age}'

object1 = Person('Tilly', 18)
print(object1)
print(object1.display_info())