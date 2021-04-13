print("----Zadanie 2 ----")
import numpy
import inquirer

#####################
# CONSTANTS
#####################

macierz_1 = [
    [4, -1, -0.2, 2],
    [-1, 5, 0, -2],
    [0.2, 1, 10, -1],
    [0, -2, -1, 4]
]
macierz_1_wynik = [
    30,
    0,
    -10,
    5,
]
"""
poprawne wyniki dla n = 1:
x1 = 7.5
x2 = 1.5
x3 = -1.3
x4 = 1.675

dla n = 2:
x1 = 6.9725
x2 = 2.0645
x3 = -1.1784
x4 = 1,98765
"""
n = 0
macierz_A = []
macierz_b = []
U = None
D = None
L = None
x = None


#####################
# FUNCTIONS
#####################
def metoda_gaussa_seidla(macierz, macierz_wynik, rozmiar, ilosc_operacji):
    global U, D, L, x
    U = numpy.zeros((rozmiar, rozmiar))
    D = numpy.zeros((rozmiar, rozmiar))
    L = numpy.zeros((rozmiar, rozmiar))
    # Devide A into L + D + U
    for i in range(rozmiar):
        for j in range(rozmiar):
            if i < j:
                U[i][j] = macierz[i][j]
            elif i > j:
                L[i][j] = macierz[i][j]
            else:
                D[i][j] = macierz[i][j]

    # Calculate D^-1
    for i in range(rozmiar):
        D[i][i] = 1 / D[i][i]

    # Calculate D^-1 * b
    for i in range(rozmiar):
        macierz_wynik[i] *= D[i][i]

    # Calculate D^-1 * L
    for i in range(rozmiar):
        for j in range(rozmiar):
            L[i][j] *= D[i][i]

    # Calculate D^-1 * U
    for i in range(rozmiar):
        for j in range(rozmiar):
            U[i][j] *= D[i][i]

    # Initialize x
    x = [0 for _ in range(rozmiar)]

    for k in range(ilosc_operacji):
        for i in range(rozmiar):
            x[i] = macierz_wynik[i]
            for j in range(i):
                x[i] -= L[i][j] * x[j]
            for j in range(i + 1, rozmiar):
                x[i] -= U[i][j] * x[j]

    print("Wynik: ")
    for i in range(rozmiar):
        print(f"x[{i + 1}] = {x[i]}")


def wczytaj_liczby():
    global macierz_A, macierz_b, n
    n = int(input("Podaj n: "))
    if n < 1:
        print("Nieprawidłowa wartość parametru n!")
    #     wczytaj macierz A

    for i in range(n):
        wiersz = []
        for j in range(n):
            liczba = float(input(f"A[{i + 1}][{j + 1}] = "))
            if liczba == 0 and i == j:
                print("wartosc na przekątnej musi być różna od 0")
                liczba = float(input(f"A[{i + 1}][{j + 1}] = "))
                wiersz.append(liczba)
            else:
                wiersz.append(liczba)
        macierz_A.append(wiersz)
        del wiersz
    #     wczytaj macierz b
    for i in range(n):
        macierz_b.append(float(input(f"b[{i + 1}] = ")))


#####################
# MAIN
#####################
print("Macierz A:")
for i in range(4):
    print(macierz_1[i])
print("Macierz b:")
for i in range(4):
    print(macierz_1_wynik[i])

questions = [
    inquirer.List(name='wybor',
                  message="Wybierz",
                  choices=["Podana macierz", "Wlasna macierz"]
                  ),
    inquirer.Text(name='ilosc_operacji',
                  message="Podaj ilosc operacji"),
]
answers = inquirer.prompt(questions)
if answers['wybor'] == "Podana macierz":
    metoda_gaussa_seidla(macierz_1, macierz_1_wynik, 4, int(answers['ilosc_operacji']))
if answers['wybor'] == "Wlasna macierz":
    wczytaj_liczby()
    metoda_gaussa_seidla(macierz_A, macierz_b, n, int(answers['ilosc_operacji']))
