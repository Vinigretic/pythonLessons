# import csv

# FILENAME = 'users.csv' # глобальная переменная(константа), всегда указываем  большими буквами
#
# users = [
#     ['Viktory', 20],
#     ['Alina', 18],
#     ['Serhii', 58]
#
# ]
# with open(FILENAME, 'w', newline='') as f:
#     a = csv.writer(f)
#     a.writerows(users)

# параметр newline, разделитель '' ставить всегда, оптимизация записи для разных ОП
# writer - записывает файл в переменную
# writerow - записывает в файл данные которые передаем как параметр, одну строку
# writerows - записывает в файл данные которые передаем как параметр, все строки
# writeheader() - записывает в файл словари

# with open(FILENAME, 'a', newline='') as f:
#     user = ['Dima', 25]
#     a = csv.writer(f)
#     a.writerow(user)

# reader() создание обьекта для чтения

# with open(FILENAME, 'r', newline='') as f:
#     a = csv.reader(f)
#     # print(*a)
#     for i in a:
#         print(i[0], '-', i[1])

# DictWriter() возвращает обьект который позваляет записывать в файл словари, принимает два параметра
# DictReader() возвращает обьект который позваляет читать из файла (для работы со словарями)

# users = [
#     {'name': 'Viktory', 'age': 20},
#     {'name': 'Yana', 'age': 21},
#     {'name': 'Dima', 'age': 35},
#     {'name': 'Max', 'age': 28}
# ]
# with open(FILENAME, 'w', newline='') as f:
#     columns = ['name', 'age']
#     a = csv.DictWriter(f,fieldnames=columns)
#     a.writeheader()
#
#     a.writerows(users)
#
# with open(FILENAME, 'r', newline='') as f:
#     a = csv.DictReader(f)
#     for i in a:
#         print(i['name'], '-', i['age'])




