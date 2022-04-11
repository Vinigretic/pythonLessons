from pprint import pprint

with open('data.txt', 'r', encoding='UTF-8') as f:
    x = f.readlines()
# x = list(map(str.rstrip, x))
pprint(x)
# задача 1 часть 1
# a = 0
# for ind, i in enumerate(x[:-1], 1):
#     if int(i) - int(x[ind]) < 0:
#         a += 1
# print(a)

# a = [int(i) for i in x]
# b = [sum(a[ind:ind + 3]) for ind, i in enumerate(a[:-1])]
# a = 0
# for ind, i in enumerate(b[:-1], 1):
#     if int(i) - int(b[ind]) < 0:
#         a += 1
# print(a)

# задача 2 часть 1


# horizon = 0
# depth = 0
# for i in x:
#     i = i.split()
#     i[-1] = int(i[-1])
#     if i[0] == 'forward':
#         horizon += i[-1]
#     elif i[0] ==  'down':
#         depth += i[-1]
#     elif i[0] == 'up':
#         depth -= i[-1]
# print(horizon * depth )

# Задача 2 часть 2

# horizon = 0
# depth = []
# aim = 0
# for i in x:
#     i = i.split()
#     i[-1] = int(i[-1])
#     if i[0] == 'forward':
#         horizon += i[-1]
#         depth.append(aim * i[-1])
#     elif i[0] ==  'down':
#         aim += i[-1]
#     elif i[0] == 'up':
#         aim -= i[-1]
# print(horizon * sum(depth))


# Задача 3, часть 1
# b = [i[j] for j in range(len(x[0])) for i in x]
# b = [[i[j] for i in x] for j in range(len(x[0]))]
#
# d = tuple(map(lambda x: tuple(map(x.count, x)), b))
# epsilon = list(map(lambda x, y: x[y.index(min(y))], b, d))
# gamma = list(map(lambda x, y: x[y.index(max(y))], b, d))
# print(epsilon)
# print(gamma)
#
# def fun(x):
#     s = [2 ** i for i in range(len(x) - 1, -1, -1)]
#     z = list(map(lambda k, y: int(k) * y, x, s))
#     e = 0
#     for i in z:
#         e += i
#     return e
#
#
# gamma_10 = fun(gamma)
# epsilon_10 = fun(epsilon)
#
# print(gamma_10 * epsilon_10)

# задача 3 часть 2
# a = x[:]
# for i in range(len(a[0])):
#     b = [i[j] for j in range(len(a[0])) for i in a]
#     b = [[i[j] for i in a] for j in range(len(a[0]))]
#     d = tuple(map(lambda x: tuple(map(x.count, x)), b))
#     gamma = list(map(lambda x, y: x[y.index(max(y))], b, d))
#     print(gamma)
#
#     x1 = a[:]
#     for j in x1:
#         # if len(a) == 2:
#         #     break
#         if gamma[i] == '1' and j[i] == '0' or gamma[i] == '0' and j[i] == '1':
#             a.remove(j)
#
#     print(a)

# for j in a:
#     if j[-1] == '0':
#         a.remove(j)
# print(a)

# x = '01' + '100110'
#
# print(max(x, key=x.count))
# попробовать с фильтром

# c = x[:]
# for i in range(len(c[0])):
#     b = [i[j] for j in range(len(c[0])) for i in c]
#     b = [[i[j] for i in c] for j in range(len(c[0]))]
#     d = tuple(map(lambda x: tuple(map(x.count, x)), b))
#     epsilon = list(map(lambda x, y: x[y.index(min(y))], b, d))
#     # print(epsilon)
#
#     x1 = c[:]
#     for j in x1:
#         if len(c) == 2:
#             break
#         if epsilon[i] == '0' and j[i] == '1' or epsilon[i] == '1' and j[i] == '0':
#             c.remove(j)
#
# print(c)
# for j in c:
#     if j[2] == '0':
#         c.remove(j)
# print(c)

# a.remove(2)  # удаляет первый найденный элемент

# задача 6 часть 1

# a = [int(j) for i in x for j in i.split(',')]
# for j in range(80):
#     a1 = a[:]
#     for ind, i in enumerate(a1):
#         for j in range(9):
#             if i == j:
#                 a[ind] = i - 1
#         if i == 0:
#             a[ind] = 6
#             a.append(8)
# print(len(a))

# задача 4 часть 1
# a = x[0]
# b = x[1:]
# desk = len(b) // 6
# # print(desk)
# c = [[list(map(int, b[j + 1 + 6 * i].split())) for j in range(5)] for i in range(desk)]
# pprint(c)
# exit()
# # a = '22 13 17 11  0'
# # print(list(map(int, a.split())))
#
# # 1, 7, 13
#
#
#
# pprint(b)

# b = [[i[j] for i in x] for j in range(len(x[0]))]