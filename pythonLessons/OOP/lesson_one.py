# Парадигмы программирования
# 1. Функциональное
# 2. Обьектно-ориентированное
# 3. Линейное

# Главные принципы ООП
# 1. Инкапсуляция
# 2. Наследование
# 3. Полиморфизм
# Дополнительный - абстракция

# Классы - это типы данных

# class Person:  # навзание класса всегда с большой буквы
#     pass
#
#
# maxim = Person()  # создание обьекта класса, создание обьекта происходит с помощью конструктора, который работает автоматически
# viktory = Person()

# class Person:
#     def say_hello(self):   # метод, все функции в классе это методы, self -это ссылка на обьекты в которых используется этот метод
#         print('Hello')
#
#     def say(self, message):
#         print(message)
#
#
# object_1 = Person()  # обьект
# object_1.say_hello() # для обьекта вызываем метод say_hello, результатом которогу будет выполенние метода(функции)
# object_1.say('Good day today')  # если в метод передаеся параметры кроме self, то при вызове, в оьект их нужно указать

# class Person:
#     def say(self, message):  # параметр self можно передать в другой метод
#         print(message)
#
#     def say_hello(self):   #  создаем другой метод и передаем в него параметр self
#         self.say('Good day today')  #  вызываем другой метод класса
#
#
# object_1 = Person()
# object_1.say_hello() # вызов метода


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


# Конструктор создает обьекты(вызывается при создании обьектов)

# class Person:
#     def __init__(self): # метод контруктора, всегда принимает self
#         print('Создание обьекта Python')
#
#
# object_1 = Person()

# class Person:
#     def __init__(self, name):  # создаем конструктор с доп параметром name - это атрибут обьекта(экземпляра),
#                                # артибуты обьекта(экземпляра) создаются
#                                # только в конструкторе, в не конструктора создаются динамические атрибуты и артибуты класса
#                                # доп параметр создаем всегда когда нам нужно что-то принимать от пользователя
#         self.name = name  # создаем артибут обьекта(экземпляра)
#         self.age = 1  # создаем атрибут обьекта(экземпляра) и присваеваем ему значение по стандарту
#
#     def display_info(self):
#         print(f'Name: {self.name}, Age: {self.age}')
#
# #
# object1 = Person('Alina')
#
# print(object1.name)
# print(object1.age)
#
# object1.age = 20
# print(object1.age)
#
# object1.name = 'Vadim'
# print(object1.name)
# #
# object1.city = 'Lviv' # динамическое создание атрибута не в конструкторе
# print(object1.city)
# #
# object1.city = 'Kyiv'  # динамические атрибуты так же можно изменять
# print(object1.city)
#
# object1.display_info()