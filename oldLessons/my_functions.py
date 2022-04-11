def super_sum(*x):
    return sum(x)


if __name__ == '__main__': # необходимо для определения откуда запускается файл, библиотека модуль
    print('cat')
    print(__name__)


def multi(*x):
    b = 1
    for i in x:
        b *= i
    return b

