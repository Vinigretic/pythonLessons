import pickle

# dump(object, file) записывает обьект object в бинарный файл
# load(file) считывает данные из бинарного файла в обьект

# FILENAME = 'user.dat'
# name = input()
# age = int(input())

# with open(FILENAME, 'wb') as f:
#     pickle.dump(name, f)
#     pickle.dump(age, f)
#
# with open(FILENAME, 'rb') as f:
#     name = pickle.load(f)
#     age = pickle.load(f)
#     print('Имя: ', name, 'возраст: ', age)

# users = [
#     ['Vika', 20, True],
#     ['Alina', 25, False],
#     ['Max', 30, False],
#     ['Dima', 35, True]
# ]
# with open(FILENAME, 'wb') as f:
#     pickle.dump(users, f)
#
# with open(FILENAME, 'rb') as f:
#     a = pickle.load(f)
#     for i in a:
#         print('Имя:', i[0], '\tВозраст:', i[1], '\tЖенат(замужем):', i[2])

