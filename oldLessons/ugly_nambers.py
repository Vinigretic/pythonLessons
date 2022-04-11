# Мерзкими числами зовутся числа, состоящие только из простых делителей 2, 3 или 5.
# Необходимо найти минимальные делители, которые должны быть простыми числами 2, 3, 5, т.е если есть еще и 7 то число не мерзкое
# Последовательность 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... показывает первые 11 мерзких чисел
# (1 тоже считается мерзким числом). Напишите программу, которая находит мерзкое число с номером n
# когда буду принтовать мерзкие числа отпринтовать рядом делители
# Входные данные: N, int.
#
# Выходные данные: Мерзкое число с номером N, int.
#
# Примеры:
#
# ugly_number(4) == 4
# ugly_number(6) == 6
# ugly_number(11) == 15
# 1
# 2
# 3
# Где используется подобное: Для демонстрации того, что простое решение может быть весьма медленным
#
# Ограничения: Входное число меньше или равно 1500
#
# def ugly_number(n: int) -> int:
#     d = 1000
#     c = []
#     for i in range(6, d + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             c.append(i)
#     # print(c)
#     # exit()
#     k = {i for i in range(1, 500) for j in [2, 3, 5] if i % j == 0}
#     s = [i for i in k for j in c if i % j == 0]
#
#     return sorted((1,) + tuple(k.difference(s)))[n - 1]


if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")


# n = 1000
# c = []
# for i in range(6, n + 1):  # нахожу простые числа
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         c.append(i)
# # print(c)
#
# k = [i for i in range(1, 500) for j in [2, 3, 5] if i % j == 0] # нахожу числа которые делятся на 2, 3 ,5
# s = [i for i in k for j in c if i % j == 0] # нахожу в списке к числа которые делятся без остатка на простые числа из списка с
#
# print(sorted((1,)+tuple(set(k).difference(s)))[20-1])
from itertools import *
# print(*product([0, 1], repeat=4))  # (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) (2, 1) (2, 2)
#
# print(*product('abc', [145]))  # ('a', 'a') ('a', 'b') ('a', 'c') ('b', 'a') ('b', 'b') ('b', 'c') ('c', 'a') ('c', 'b') ('c', 'c')
# print(*combinations('abc', 2))  # ('a', 'b') ('a', 'c') ('b', 'c')
# print(*combinations_with_replacement('abc', 2))  # ('a', 'a') ('a', 'b') ('a', 'c') ('b', 'b') ('b', 'c') ('c', 'c')
# print(*combinations_with_replacement([2, 3, 5], 3))  # (2, 2, 2) (2, 2, 3) (2, 2, 5) (2, 3, 3) (2, 3, 5) (2, 5, 5) (3, 3, 3) (3, 3, 5) (3, 5, 5) (5, 5, 5)
# print(*permutations('abc', 2)) #('a', 'b') ('a', 'c') ('b', 'a') ('b', 'c') ('c', 'a') ('c', 'b')

