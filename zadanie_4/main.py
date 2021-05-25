import numpy as np
import functions as fn
import inquirer

# functions
f1 = lambda x: np.sqrt(5 * x ** 5 + x ** 4)
f2 = lambda x: 3 * x ** 3 - x ** 2 - 5
f3 = lambda x: np.abs(x)
f4 = lambda x: np.cos(x ** 2)
f5 = lambda x: 21 * x - 37

funcs = [f1, f2, f3, f4, f5]

questions = [
    inquirer.List(name='wybor_funkcji',
                  message="Wybierz: ",
                  choices=["np.sqrt(5 * x ** 5 + x ** 4)", "3 * x ** 3 - x ** 2 - 5", "np.abs(x)", "np.cos(x ** 2)",
                           "21 * x - 37"]),

    inquirer.Text(name='epsilon',
                  message="Podaj dokladnosc"),

    inquirer.Text(name='przedzial_1',
                  message="Podaj poczatek przedzialu: "),

    inquirer.Text(name='przedzial_2',
                  message="Podaj koniec przedzialu: "),

    inquirer.Text(name='ilosc_wezlow',
                  message="Podaj ilosc wezlow: "),

]
answers = inquirer.prompt(questions)

if answers['wybor_funkcji'] == "np.sqrt(5 * x ** 5 + x ** 4)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f1, int(answers['przedzial_1']), int(answers['przedzial_2']), float(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f1))

if answers['wybor_funkcji'] == "3 * x ** 3 - x ** 2 - 5":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f2, int(answers['przedzial_1']), int(answers['przedzial_2']), float(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f2))

if answers['wybor_funkcji'] == "np.abs(x)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f3, int(answers['przedzial_1']), int(answers['przedzial_2']), float(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f3))

if answers['wybor_funkcji'] == "np.cos(x ** 2)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f4, int(answers['przedzial_1']), int(answers['przedzial_2']), float(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f4))

if answers['wybor_funkcji'] == "21 * x - 37":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f5, int(answers['przedzial_1']), int(answers['przedzial_2']), float(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f5))
