import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib import animation

DATA_FILE = 'data1.csv'
def compare_multiplication_speed():
    print("1. Сравнение скорости стандартного умножения и умножения с помощью библиотеки NumPy")
    case_one_start_time = time.perf_counter()
    random_list_one = [round(random.random() * 10, 0) for _ in range(1_000_000)]
    random_list_two = [round(random.random() * 10, 0) for _ in range(1_000_000)]
    
    multiplied = [a * b for a, b in zip(random_list_one, random_list_two)]
    case_one_time = time.perf_counter() - case_one_start_time
    print(f'Время, затраченное на стандартное умножение: {case_one_time}')
    case_two_start_time = time.perf_counter()
    random_list_one = np.random.randint(0, 100, (1, 1), dtype='int64')
    random_list_two = np.random.randint(0, 100, (1, 1000000), dtype='int64')
    multiplied = np.multiply(random_list_one, random_list_two)
    case_two_time = time.perf_counter() - case_two_start_time
    print(f'Время, затраченное на умножение с использованием NumPy: {case_two_time}')



def plot_csv_data(file_name):
    print("2. Операции с CSV-файлами и построение графика")
    arr = np.genfromtxt(DATA_FILE, delimiter=';')
    x = arr[:, 0]
    y1 = arr[:, 3]
    y2 = arr[:, 17]

    fig, ax = plt.subplots()
    ax.plot(x, y1, color='blue', label='График 1')
    ax.plot(x, y2, color='red', label='График 2')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_title('График')
    ax.legend()
    plt.show()

    corr = np.corrcoef(y1, y2)[0, 1]
    plt.scatter(y1, y2)
    plt.title("График корреляции Y1 и Y2")
    plt.xlabel("Y1")
    plt.ylabel("Y2")
    plt.legend(["Данные"])
    plt.plot([min(y1), max(y1)], [min(y2), max(y2)], 'r--')
    plt.show()


def plot_3d_function():
    print('3. Построение 3D-графика X, Y и Z.')
    x = np.linspace(-5 * np.pi, 5 * np.pi)
    y = np.cos(x)
    z = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, c='blue')
    plt.show()


# Доп
def animate_sine_wave():
    fig, ax = plt.subplots()

    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)
    line, = plt.plot(x, y)

    def animated(i):
        line.set_ydata(np.sin(x + i / 30))
        return line,

    anim = animation.FuncAnimation(fig, animated, interval=10, blit=True, save_count=20)

    plt.show()


if __name__ == "__main__":
    compare_multiplication_speed()
    plot_csv_data(DATA_FILE)
    plot_3d_function()
    animate_sine_wave()