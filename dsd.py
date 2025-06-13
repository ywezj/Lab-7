import matplotlib.pyplot as plt

# Данные
x = [0.0356, 0.0402, 0.0459, 0.0526, 0.0604, 0.0319]
y = [3.1046, 3.5295, 4.0453, 4.6916, 5.3764, 2.7679]

# Построение графика
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Добавление подписей
plt.title('График по точкам')
plt.xlabel('x')
plt.ylabel('y')

# Отображение графика
plt.grid(True)
plt.show()