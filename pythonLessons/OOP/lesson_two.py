# Инкапсуляция - предотвращает прямой доступ к обьктам из вызывающего кода
# Принцип ООП который предоставляет нам возможность реализации приватных атрибутов для предотвращения некоректного ввода
# Позволяет сделать атрибуты приватными. К приватным атрибутам мы можем обратится только внутри класса, т.е динамически их
# поменять  нельзя. Обратится к таким атрибутам можно только с помощью доп методов, которые будут их возвращать

# Атрибуты в Python являются общедоступными и мы можем вызвать или изменить его из любого места программы

# Анотации свойств пишется перед геттером и сеттером. Применяется всегда когда есть какая-то проверка условия

# Геттер - имеет анотацию @property
# Сеттер - имеет анотацию @имя_геттера.setter
# Геттер и сеттер всегда называются одинаково
# Свойсто геттер определяется перед сеттером

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#
#     def display_info(self):
#         print(f'Как тебя зовут: {self.name}, Сколько тебе лет: {self.age}')
#
#
# object1 = Person('Valy')
# object1.display_info()
#
# object1.name = 'Lyci'
# object1.display_info()
#
# object1.age = -120
# object1.display_info()

# Пример неправильного кода

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # создание приватного атрибута
#         self.__age = age
#
#     def set_age(self, age):  # метод проверки Сеттер или мьютейтор, нужет для того что бы в зависимости от возраста, определять
#         if 0 < age < 150:    # какой участок кода отработает
#             self.__age = age
#         else:
#             print('Некоректный ввод возраста')
#
#     def get_age(self):  # с помощью этого метода мы обращаемся к атрибутам, этот метот называют Геттер или аксессор
#         return self.__age  # их так называют потому что они возвращают атрибуты
#
#     def get_name(self):  # с помощью этого метода мы обращаемся к атрибутам, этот метот называют Геттер или аксессор
#         return self.__name  # их так называют потому что они возвращают атрибуты
#
#     def display_info(self):
#         print(f'Как тебя зовут: {self.__name}, Сколько тебе лет: {self.__age}')
#
# object1 = Person('Valy', 160)
# object1.get_name()
# object1.set_age(160)
# object1.get_age()
#
# print(object1.get_name())
# print(object1.get_age())

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 150:
#             self.__age = age
#         else:
#             print('Некоректный ввод возраста')
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Как тебя зовут: {self.__name}, Сколько тебе лет: {self.__age}')
#
# object1 = Person('Lena', 25)
# object1.display_info()
# object1.age = -12
# print(object1.age)
# object1.age = 35
# object1.display_info()

# Написати клас автомобіль який має поля конструктора(атрибути): рік авто, модель, країна випуску.
# Написати гетер+сетер для року випуску і країна випуску (Якщо є в лісті з списком країн то можна змінювати)
# і гетер для модель. Створити два обєкти з різними авто, протестити


# class Car:
#     def __init__(self, year, model, country):
#         self.__year = year
#         self.__model = model
#         self.__country = country
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         if 1886 <= year <= 2022:
#             self.__year = year
#         else:
#             print('Некорректный год выпуска')
#
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, country):
#         if country in ['French', 'Chaina', 'Japan', 'Germany', 'Italy', 'СPCР']:
#             self.__country = country
#         else:
#             print('Некоректная страна производитель')
#
#     @property
#     def model(self):
#         return self.__model
#
#     def display_info(self):
#         print(f'Модель машины: {self.__model}, год выпуска: {self.__year}, страна производитель: {self.__country}')
#
#
# object1 = Car(2008, 'Toyta', 'Japan')
# object2 = Car(2011, 'Mersedes', 'Germany')
# object1.display_info()
# object2.display_info()
# object1.year = 1700
# object2.country = 'Ukrain'
# object1.year = 2005
# object1.display_info()

# магазин одежды, список вещей которые есть в наличии, размеры, время заказа

# class Shop_close:
#     def __init__(self, things, size, time_work):
#         self.__things = things
#         self.__size = size
#         self.__time_work = time_work
#
#     @property
#     def things(self):
#         return self.__things
#
#     @things.setter
#     def things(self, things):
#         if things in ['jeans', 'dress', 'shirt']:
#             self.__things = things
#         else:
#             print('К сожалению таких вещей нет в магазине')
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size in ['xs', 's', 'm', 'l', 'xl', 'xxl']:
#             self.__size = size
#         else:
#             print('Такого размера нет')
#
#     @property
#     def time_work(self):
#         return self.__time_work
#
#     @time_work.setter
#     def time_work(self, time_work):
#
#         if time_work in range(10, 21):
#             self.__time_work = time_work
#         else:
#             print('Извините магазин не работает')
#
#
#     def display_info(self):
#         print(f'Ваш выбор: {self.__things}, ваш размер: {self.__size}, время пакупки: {self.__time_work}')
#
#
# object1 = Shop_close('dress', 'm', 12)
# object1.display_info()
# object1.things = 'hat'
# object1.display_info()
# object1.size = 'xn'
# object1.time_work = 8
# object1.display_info()







