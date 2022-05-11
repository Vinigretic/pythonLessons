# Полиморфизм - это когда от типа обьекта зависит поведение класса

# isinstance(object, type)

class Person:  # создвем класс Person
    def __init__(self, name):  # описываем метод конструктор, с атрибутом name
        self.__name = name # описываем атрибут name

    @property  # описываем геттер для атрибута name
    def name(self):  # описываем метод который возвращает атрибут
        return self.__name

    def do_nothing(self):  # описываем метод работы класса Person
        print(f'Человек: {self.__name} не работает')

class Employee(Person):  # создаем класс Employee который наследуется от класса Person
    def work(self):  # описываем метод работы класса Employee
        print(f'Человек: {self.name} работает')

class Student(Person):  # создаем класс Student который наследутся от класса Person
    def study(self):  # описываем метод работы класса Student
        print(f'Человек: {self.name} учится')


def act(class_name):  # создаем функцию в которой проверяем типы
    if isinstance(class_name, Student):  #если в переменную функции class_name заходит класс Student, условие выполняется
        class_name.study()  # вызываем метод класса Student
    elif isinstance(class_name, Employee):  #если в переменную функции class_name заходит класс Employee, условие выполняется
        class_name.work()  # вызываем метод класса Employee
    elif isinstance(class_name, Person):  #если в переменную функции class_name заходит класс Person, условие выполняется
        class_name.do_nothing()  # вызываем метод класса Person


object1 = Employee('Willy')  # создаем обьект который принимает класс Employee
object2 = Student('Polly')
object3 = Person('Holly')


act(object1)  # передаем в функцию object1 который содержит класс
act(object2)
act(object3)