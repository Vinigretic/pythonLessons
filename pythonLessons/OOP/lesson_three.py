# Наследование позволяет создавать класс на основе уже существующего класса
# Ключевое понятие наследования - подкласс и супер класс
# Подкласс(дочерний класс, child класс) - наследует от супер класса все публичные атрибуты и методы
# Супер класс (базовый класс или родительский класс) - класс который прописывается за основу

# class Название_подкласса(Название_супер_класса):
#     методы подкласса

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя: {self.__name}')
#
#
# class Employee:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя: {self.__name}')
#
#
#     def work(self):
#         print(f'Человек {self.__name} работает')
#
# object1 = Person('Elina')
# object2 = Employ('Elina')
# object1.display_info()
# object2.display_info()
# object2.work()

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя :{self.__name}')
#
#
# class Employee(Person):
#     def work(self):
#         print(f'Человек {self.name} работает')
#
# object1 = Employee('Elina')
# object1.display_info()
# object1.work()

# Множественное наследование
# Работает только в том случае если в наследуемых классах есть только один конструктор

# class Employee:
#     def work(self):
#         print('Работник работает')
#
# class Student:
#     def study(self):
#         print('Студент учится')
#
# class WorkingStudent(Employee, Student):
#     pass
#
# object1 = WorkingStudent()
# object1.work()
# object1.study()


# ПРИМЕР НЕПРАВИЛЬНОГО РЕШЕНИЯ

# class MotoBike:
#     def __init__(self, name_owner, age, model):
#         self.__name_owner = name_owner
#         self.__age = age
#         self.__model = model
#
#     @property
#     def name_owner(self):
#         return self.__name_owner
#
#     @name_owner.setter
#     def name_owner(self, name_owner):
#         if name_owner in ('Max', 'Lena', 'Vita', 'Evgen', 'Sofi', 'Serhii'):
#             self.__name_owner = name_owner
#         else:
#             print('Вы не являетесь владельцем')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1885, 2023):
#             self.__age = age
#         else:
#             print('Мотоцикл еще не изобрели')
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if model in ('Карпаты', 'Ява', 'Kawasaky'):
#             self.__model = model
#         else:
#             print('Этой модели нет в наличии')
#
#
#     def display_info(self):
#         print(f'Владелец: {self.__name_owner}, год выпуска: {self.__age}, модель: {self.__model}')
#
#
# class Car:
#     def __init__(self, brand, country):
#         self.__brand = brand
#         self.__country = country
#
#     @property
#     def brand(self):
#         return self.__brand
#
#     @brand.setter
#     def brand(self, brand):
#         if brand in ('Mersedes', 'BMW', 'Hunday', 'Honda', 'Ford'):
#             self.__brand = brand
#         else:
#             print('Данной модели нет в наличии')
#
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, country):
#         if country in ('Germany', 'Korey', 'Japan', 'USA'):
#             self.__country = country
#         else:
#             print('Страна не является производителем')
#
#     def display(self):
#         print(f'Производитель: {self.__brand}, страна: {self.__country}')
#
#
#
# class Transport(MotoBike, Car):
#     pass
#
# object1 = Transport('Max', 2000, 'Ява')
# object1.display()



