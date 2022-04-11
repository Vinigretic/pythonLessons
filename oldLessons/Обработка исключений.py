# Обработка исключений (ошибок)
# try:
#     # Здесь условно проблемный код, который может вызвать ошибку
#     raise ValueError('Закончились попытки!')
# except (Тип исключения, ...):
#     # код выполниться если совпадёт тип исключения с одним из перечисленных типов
# except Тип исключения 2:
#     # код при Исключении 2
# except:
#     # код будет выолнен при любом исключении
# else:
#     # код выполнится, если не было поймано ни одного мключения
# finally:
#     # будет выполнено в любом случае

# number = input('Введите целое число: ')
# try:
#     number = int(number)
#     number2 = 10 / number
# except ValueError:
#     print('Это не целое число!')
# except ZeroDivisionError:
#     print('Делить на ноль нельзя!')
# else:
#     print(number2)

# except ValueError:
#     number2 = 'Это не целое число!'
# except ZeroDivisionError:
#     number2 = 'Делить на ноль нельзя!'
# print(number2)

# while True:
#     try:
#         number = int(input('Введите целое число: '))
#         break
#     except ValueError:
#         print('Это не целое число!')
# print(number * 10)

# raise ValueError('Закончились попытки!') # искуственный вызов исключения(ошибки)
