# Графики matplotlib
import matplotlib.pyplot as plt
# plt.plot((0, 3, 1, 2, 1, 5, 4, 0))
# plt.plot((1, 3, 1, 2, 1, 5, 4, -2))
# plt.show()

# Задаём вручную ось y: ??????? ПОЧЕМУ ОСЬ У
# plt.plot((-0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3), (0, 3, 1, 2, 1, 5, 4, 0))
# plt.plot((0.15, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3), (15, 3, 1, 2, 1, 5, 4, 0))
# plt.show()

# Строим замкнутую фигуру:
# plt.plot((0, 0, 5, 4, 0), (0, 3, 2, 1, 0))
# plt.plot((1, 0, 5, 4, 3, 1), (1, 3, 2, 1, 0, 1))
# plt.show()

# Пример треугольника в прямоугольнике:
# plt.plot((0, 0, 1, 1, 0), (0, 1, 1, 0, 0))
# plt.plot((0, 0, 4, 4, 0), (0, 4, 4, 0, 0))
# plt.plot((0.1, 0.5, 0.9, 0.1), (0.1, 0.9, 0.1, 0.1))
# plt.plot((1, 2, 2, 1), (1, 3, 1, 1))
# plt.show()

# 2. Множество точек:
# plt.scatter([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])
# plt.scatter([1, 2, 3, 1, 2, 1], [2, 3, 4, 3, 4, 4])
# plt.scatter([2, 3, 4, 3, 4, 4], [1, 2, 3, 1, 2, 1])
# plt.scatter((1, 8, 5, 3), (0, 4, 7, 9))
# plt.show()

# 3. Гистограммы:
# 3.1. Вертикальная:
# plt.bar([6, 7, 10], [10, 15, 21])
# plt.show()
# 3.2. Горизонтальная:
# plt.barh([6, 7, 8], [10, 15, 21])
# plt.show()
# 3.3. Отображаем несколько наборов данных:
# plt.bar([6, 7, 8], [10, 15, 21])
# plt.bar([6, 7, 8], [6, 12, 17])
# plt.show()
# 3.4. Указываем ширину со смещением:
# plt.bar([5.9, 6.9, 7.9], [10, 15, 21], width=0.2)
# plt.bar([6.1, 7.1, 8.1], [6, 12, 17], width=0.2)
# plt.bar([5.9, 6.9, 7.9], [10, 15, 21], width=0.8)
# plt.bar([6.1, 7.1, 8.1], [6, 12, 17], width=0.2)
# plt.show()
# 4. Круговые диаграмы:
# plt.pie([5, 13, 21, 27, 10, 17])
# plt.pie([5, 10, 3, 20, 0.1])
# plt.show()
# 5. Японские свечи (ящик с усами)
# plt.boxplot([1, 5, 7, 4, 6, 10, 20, -6])  # min - max начало и конец, оранжевая линия медиана от суммы эл-тов массива,
# линия до медианы(граница свечи) 25% от от суммы эл-тов массива, линия выше 75%
# елементы массива которые сильно отличаются от основой массы они будут выбросами
# plt.boxplot([1, 5, 7, 15, 8, 10, 20, -6, 40])
# plt.show()
# plt.boxplot([
#     [1, 5, 7, 4, 6, 10, 15],
#     [-2, 5, 7, 4, 6, 10, 15],
#     [-4, 5, 7, 4, 6, 10]
# ])
# plt.show()
# 6. Меняем цвет figure и axes(оси)
# fig = plt.figure() # создание обьекта
# ax = fig.add_subplot(111)  # создание графика(111 - это первая срока, первый столбец и первая ячейка на сетке)
# ap = fig.add_subplot(428)
# plt.show()
# fig.set_facecolor('green')  # указываем цвет фигуры
# ax.set(facecolor='red')  # указываем цвет графика
# ap.set(facecolor='blue')
# plt.show()
# Параметры графика
# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.set_facecolor('green')
# ax.set_facecolor('red')
# ax.set_xlim([-10, 10]) # разметка ось х
# ax.set_ylim([-2, 2])  # разметка ось у
# ax.set_title('Основы анатомии графика') # называем график
# ax.set_xlabel('ось абцис') # называем оси
# ax.set_ylabel('ось ординат') # называем оси

# То же через параметры:
# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.set(facecolor='green')
# ax.set(
#     facecolor='red',
#     xlim=[-10, 10],
#     ylim =[-2, 2],
#     title='Основы анатомии графика',
#     xlabel='ось абцис',
#     ylabel='ось ординат'
# )

# 2 способа задания set
# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.set_facecolor('green')
# ax.set_facecolor('red')
#
# # 1
# ax.set_title('Основы анатомии графика')
# ax.title.set_color('white')
# ax.title.set_size(20)
# plt.show()

# 2
# ax.set_title('Основы анатомии графика', color='white', size=20)

# 7. Отображение данных на графике:
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], color='black', linewidth=10)
# ax.scatter([0, 1, 2, 3, 4], [1, 3, 8, 12, 25], color='blue', marker='*')
# plt.show()
# 8. Несколько Axes на одной Figure
fig = plt.figure()
ax_1 = fig.add_subplot(3, 2, 1)
ax_2 = fig.add_subplot(3, 2, 4)
ax_3 = fig.add_subplot(3, 2, 5)

ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_3.set(title='ax_3', xticks=[], yticks=[])
plt.show()


# fig = plt.figure()
# ax_1 = fig.add_subplot(3, 1, 1)
# ax_2 = fig.add_subplot(3, 2, 4)
# ax_3 = fig.add_subplot(3, 3, 9)
# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])




# fig = plt.figure()
# ax_1 = fig.add_subplot(3, 1, 1)  # первое - количество строк, второе - количество столбцов, третье - индекс ячейки
# ax_2 = fig.add_subplot(6, 3, 2)
# ax_3 = fig.add_subplot(3, 3, 4)
# ax_4 = fig.add_subplot(3, 3, 6)
# ax_5 = fig.add_subplot(3, 4, 10)
# ax_6 = fig.add_subplot(5, 5, 25)
# ax_1.set(title='ax_1', xticks=[], yticks=[])
# ax_2.set(title='ax_2', xticks=[], yticks=[])
# ax_3.set(title='ax_3', xticks=[], yticks=[])
# ax_4.set(title='ax_4', xticks=[], yticks=[])
# ax_5.set(title='ax_5', xticks=[], yticks=[])
# ax_6.set(title='ax_6', xticks=[], yticks=[])
#
#
#
# plt.show()



