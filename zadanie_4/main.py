import numpy as np
import functions as fn
import inquirer

# functions
f1 = lambda x: x / np.sqrt(9 + x ** 4)
f2 = lambda x: 3 * x ** 2
f3 = lambda x: np.abs(2 * x)
f4 = lambda x: np.sin(x)
f5 = lambda x: 2 * x - 7

funcs = [f1, f2, f3, f4, f5]

questions = [
    inquirer.List(name='wybor_funkcji',
                  message="Wybierz: ",
                  choices=["np.sqrt(9 + x**4)", "3*x**2", "np.abs(2*x)", "np.sin(x) + 1", "2*x - 7"]
                  ),
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

if answers['wybor_funkcji'] == "np.sqrt(9 + x**4)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f1, int(answers['przedzial_1']), int(answers['przedzial_2']), int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f1))

if answers['wybor_funkcji'] == "3*x**2":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f2, int(answers['przedzial_1']), int(answers['przedzial_2']), int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f2))

if answers['wybor_funkcji'] == "np.abs(2*x)":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f3, int(answers['przedzial_1']), int(answers['przedzial_2']), int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f3))

if answers['wybor_funkcji'] == "np.sin(x) + 1":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f4, int(answers['przedzial_1']), int(answers['przedzial_2']), int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f4))

if answers['wybor_funkcji'] == "2*x - 7":
    print("Wynik (Metoda Simspsona): ")
    print(fn.simpson(f5, int(answers['przedzial_1']), int(answers['przedzial_2']), int(answers['epsilon'])))

    print("Wynik (Metoda Legendre'a): ")
    print(fn.legendre_gauss(int(answers['ilosc_wezlow']), int(answers['przedzial_1']), int(answers['przedzial_2']), f5))
