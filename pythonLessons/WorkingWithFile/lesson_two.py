# При работе с текстовыми файлами, в файл всегда записывается только строка

# with open('hello.txt', 'w') as h:
#     h.write('Hello')

# with open('hello.txt', 'a') as h:
#     h.write('world')

# with open('hello.txt', 'a') as h:
#     h.write('\nHello, Vika')

# with open('hello.txt', 'w') as h:
#     print('Hello world', file=h)  # запись в файл, второй вариант

# Способы считивания файлов:
# 1. readline() - считывает одну строку из файла(по умолчанию первую)
# принцип работы метода readline в цикле

# with open('hello.txt', 'r') as h:
#     for i in h:
#         print(i, end='')  # по умолчанию строки разделяются \n, меняем на пустую строку

# with open('hello.txt', 'r') as h:
#     str1 = h.readline()
#     print(str1, end='')
#     str2 = h.readline()
#     print(str2, end='')

# with open('hello.txt', 'r') as h:
#     str1 = h.readline()
#     while str1:
#         print(str1, end= '')
#         str1 = h.readline()

# 2. read() - считывает все содержимое файла в одну строку, записывает в переменную одной строкой

# with open('hello.txt', 'r') as h:
#     str1 = h.read()
#     print(str1)


# 3. readlines() - считывает все строки файла в список

# with open('hello.txt', 'r') as h:
#     str1 = h.readlines()
#     print(str1)

# with open('hello.txt', encoding='UTF-8') as h:
#     text = h.read()
#     print(text)

# email = input('Введите email')
# password1 = input('Ввведите пароль')
# password2 = input('Ввведите пароль повторно')
# data1 = [email, password1, password2]
# with open('user.txt', 'w', encoding= 'utf8') as u:
#     for i in data1:
#         u.write(i + '\n')
#
# with open('user.txt', encoding='utf8') as u:
#     str1 = u.readlines()
#     if str1[1].strip() == str1[2].strip():
#         print('пользователь', str1[0].strip(), 'успешно авторизован')
#     else:
#         print('Неверный пароль')


