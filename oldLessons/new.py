# def ugly_number(n: int) -> int:
#     c = [1]
#     for i in range(2, 50):
#         b = i
#         k = []
#         while True:
#             for j in [2, 3, 5]:
#                 if i % j == 0:
#                     i //= j
#                     k.append(j)
#                     break
#             else:
#                 if i == 1:
#                     c.append(b)
#                     print(b, k)
#                 break
#     return c[n - 1]
#
#
# print(ugly_number(6))

# i > 1
# 8 - 4, 2, 1
# 15 - 5, 1
# 14 = 7,
from itertools import combinations_with_replacement, starmap
def fun(a):
    for i


print(fun((2, 3, 5)))
exit()

b = []
for i in range(1, 5):
    b.extend(combinations_with_replacement([2, 3, 5], i))
print(b)
print(sorted(b))

# print(*combinations_with_replacement([2, 3, 5], 35))