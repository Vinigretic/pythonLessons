class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Имя: {self.__name}')

class Employee(Person):
    def __init__(self, name, company):  # Если в родительском и дочернем классе есть конструктор, мы должны родительский
                                        # конструктор переопределить в дочернем классе, указав все атрибуты род. конструктора
                                        # в дочернем кон-ре и вызвать функию super()
        super().__init__(name)  # функция которая переопределяет конструктор класса Person, передаем все атрибуты род класса
        self.company = company

    def display_info(self):
        super().display_info()  # Если в родительском и дочернем классе есть методы, мы должны родительский
                                # метод переопределить в дочернем классе, вызвав c помощью функцию super() нужный метод

        print(f'Компания: {self.company}')

    def works(self):
        print(f'Человек {self.name} работает')

object1 = Employee('Vika', 'Apple')
object1.display_info()
