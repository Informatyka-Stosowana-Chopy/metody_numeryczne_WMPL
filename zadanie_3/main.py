from copy import copy
import inquirer
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

rzad = []


def get_diff_table(X, Y):
    """
         Get the market insert
    """
    n = len(X)
    A = np.zeros([n, n])

    for i in range(0, n):
        A[i][0] = Y[i]

    for j in range(1, n):
        for i in range(j, n):
            A[i][j] = (A[i][j - 1] - A[i - 1][j - 1]) / (X[i] - X[i - j])

    return A


def newton_interpolation(X, Y, x):
    """
         Calculate the interpolation of x points
    """
    sum = Y[0]
    temp = np.zeros((len(X), len(X)))
    #
    for i in range(0, len(X)):
        temp[i, 0] = Y[i]
    temp_sum = 1.0
    for i in range(1, len(X)):
        # x polynomial
        temp_sum = temp_sum * (x - X[i - 1])
        #
        for j in range(i, len(X)):
            temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (X[j] - X[j - i])
        sum += temp_sum * temp[i, i]
    return sum


def funkcja_wielomianowa(x, y, n):  # x, y - wiadomo n - ilość węzłów
    # interpolacyjny
    pom = []
    global rzad
    # dla 1 rzędu
    for i in range(n - 1):
        pom.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
    rzad.append(copy(pom))
    pom.clear()
    # dla kolejnych rzędów
    for _ in range(n - 2):
        for i in range(n - 2 - _):
            pom.append((rzad[_][i + 1] - rzad[_][i]) / (x[i + 2 + _] - x[i]))
        rzad.append(copy(pom))
        pom.clear()

    # wypisanie wyniku
    s = f"W(x) = {y[0]}"
    f = f""
    for i in range(n - 1):
        for j in range(i + 1):
            if x[j] < 0:
                f += f"(x + {abs(x[j])})"
            else:
                f += f"(x - {x[j]})"

        s += f" + {rzad[i][0]}{copy(f)}"
        f = f""

    return s


X = []
Y = []


def wczytaj():
    global X, Y
    with open("dane_X.txt", "r") as reader:
        X = [int(number) for number in reader.read().split(", ")]

    with open("dane_Y.txt", "r") as reader:
        Y = [int(number) for number in reader.read().split(", ")]


########################
# MAIN
########################
questions = [
    inquirer.List(name="choice", message='Jaką funkcje chcesz wybrać?', choices=['liniowa', 'wielomianowa'])
]
answers = inquirer.prompt(questions)
wczytaj()
if answers['choice'] == 'wielomianowa':
    print(funkcja_wielomianowa(X, Y, 7))
    A = get_diff_table(X, Y)
    df = pd.DataFrame(A)
    df

    xs = np.linspace(np.min(X), np.max(X), 1000, endpoint=True)
    ys = []
    for x in xs:
        ys.append(newton_interpolation(X, Y, x))

    plt.title("newton_interpolation")
    plt.plot(X, Y, 's', label="original values")  # blue dot indicates the original value
    plt.plot(xs, ys, 'r', label='interpolation values')  # Interpolation curve
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)  # specifies the position of the legend in the lower right corner
    plt.show()

if answers['choice'] == 'liniowa':
    plt.plot(X, Y, 's', label="original values")  # blue dot indicates the original value
    plt.plot(X, Y, 'r', label='interpolation values')  # Interpolation curve
    plt.show()
