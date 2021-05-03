from copy import copy
from math import pi

print("----Zadanie 3 ----")

####################################
# CONSTANT
####################################
wezel_przykladowy = [-2, -1, 0, 2, 4]
y_przykladowy = [-1, 0, 5, 99, -55]
rzad = []  # tutaj będą zapisywane tablice w każdym rzędzie i rząd[i] to będzie tablica
x_global = []
y_global = []


####################################
# FUNCTIONS
####################################
def wczytaj_wezel():
    # to potem (może)
    x_global.append(input("Podaj pierwszy węzeł: "))


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


def funckja_liniowa(x):
    pass


def funkcja_trygonometryczna(n):
    if n % 2 == 0:
        p = 0.5 * n
    else:
        p = 0.5 * (n - 1)

    a = []
    b = []

    for k in range(n):
        x_global.append((2 * k * pi) / (n + 1))

    for i in range(p):
        a.append((2 / (n + 1)) * sum())
        if i > 0:
            b.append(2 / (n + 1))  # TODO


def funkcja_modul(x):
    pass


####################################
# MAIN
####################################
# print(funkcja_wielomianowa(wezel_przykladowy, y_przykladowy))
funkcja_trygonometryczna(4)
