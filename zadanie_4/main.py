import numpy as np
import functions as fn
import matplotlib.pyplot as plt
import inquirer

# functions
f1 = lambda x: x / np.sqrt(9 + x ** 4)
f2 = lambda x: 3 * x ** 2
f3 = lambda x: np.abs(2 * x)
f4 = lambda x: np.sin(x) + 1
f5 = lambda x: 2 * x - 7

# simpson
# w = fn.simpson(f1, 0, 2, 0.01)
# print(w[0])

# x = np.linspace(-1, 1, 10)
# print( fn.legendre_gauss(4, -1, 1, f4))


questions = [
    inquirer.List(name='wybor_funkcji',
                  message="Wybierz: ",
                  choices=["np.sqrt(9 + x**4)", "3*x**2", "np.abs(2*x)", "np.sin(x) + 1", "2*x - 7"]
                  ),
    inquirer.Text(name='epsilon',
                  message="Podaj dokladnosc"),
]
answers = inquirer.prompt(questions)

if answers['wybor_funkcji'] == "np.sqrt(9 + x**4)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f1, 0, 2, int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(4, -1, 1, f1))

if answers['wybor_funkcji'] == "3*x**2":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f2, 0, 2, int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(4, -1, 1, f2))

if answers['wybor_funkcji'] == "np.abs(2*x)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f3, 0, 2, int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(4, -1, 1, f3))

if answers['wybor_funkcji'] == "np.sin(x) + 1":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f4, 0, 2, int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(4, -1, 1, f4))

if answers['wybor_funkcji'] == "2*x - 7":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f5, 0, 2, int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(4, -1, 1, f5))
