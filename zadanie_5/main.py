print("----Zadanie 5 ----")
from wzory import wartosc_funkcji, wzor_funkcji
import numpy as np
import pylab as pb
import inquirer
from aproksymacje import blad_aproksymacji, lista_wspolczynnikow, wartosc_wielomianu
import wielomian

tab_wsp = []
stopien_apro = 0

questions = [
    inquirer.List(name='wybor_funkcji',
                  message="Wybierz funkcje: ",
                  choices=["3*x-5", "|x|", "x^4-x^3-x^2-x+1", "sin(x)", "cos(x)-x^3"]),

    inquirer.Text(name='wezly',
                  message="Podaj liczbe wezlow kwadratury Gaussa <2:5>: "),

    inquirer.List(name='kryterium',
                  message="Dokonaj wyboru kryterium aproksymacji: ",
                  choices=["Kryterium dokladnosci", "Kryterium stopnia wielomianu aproksymujacego"]),
]
answers = inquirer.prompt(questions)

questions2 = [
    inquirer.Text(name='blad',
                  message="Podaj oczekiwany maksymaly blad aproksymacji: "),
]

questions3 = [
    inquirer.Text(name='stopien',
                  message="Podaj stopien wielomianu aproksymacyjnego: "),
]

if answers["kryterium"] == "Kryterium dokladnosci":
    answers2 = inquirer.prompt(questions2)
    stopien_apro = 1
    dokladnosc = True
    while dokladnosc:
        tab_wsp = lista_wspolczynnikow(answers["wybor_funkcji"], int(answers["wezly"]), stopien_apro)
        if blad_aproksymacji(answers["wybor_funkcji"], stopien_apro, tab_wsp, int(answers["wezly"])) < float(answers2["blad"]):
            dokladnosc = False
        else:
            stopien_apro += 1

if answers["kryterium"] == "Kryterium stopnia wielomianu aproksymujacego":
    answers3 = inquirer.prompt(questions3)
    stopien_apro = int(answers3["stopien"])
    tab_wsp = lista_wspolczynnikow(answers["wybor_funkcji"], int(answers["wezly"]), stopien_apro)

arg = np.linspace(-1, 1, 1000)
pb.plot(arg, wartosc_funkcji(arg, answers["wybor_funkcji"]), label='funkcja aproksymowana')
pb.plot(arg, wartosc_wielomianu(stopien_apro, arg, tab_wsp), label='aproksymacja', linestyle=':')
pb.xlabel("x")  # opis osi x
pb.ylabel("y")  # opis osi y
fig = pb.gcf()
fig.canvas.set_window_title('Wykres')
pb.grid(True)
pb.legend(loc='upper right')  # tworzy legendę wykresu
wzor_apro = wielomian.Polynomial(tab_wsp[::-1])
print("""Wzor wielomianu aproksymacyjnego: 
{}
""".format(wzor_apro))
print("Blad aproksymacji: {}".format(blad_aproksymacji(answers["wybor_funkcji"], stopien_apro, tab_wsp, int(answers["wezly"]))))
pb.title("f(x) = " + str(wzor_funkcji(answers["wybor_funkcji"])))
pb.show()

