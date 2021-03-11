import inquirer
import time

print("----Zadanie 1 ----")


#######################################
# FUNCTION
#######################################

def funkcja_wielomianowa(x):
    return x ** 2 - 1


def funkcja_trygonometryczna(x):
    pass


def funkcja_wykladnicza(x):
    pass


def oblicz_bisekcja(funkcja, a, b, kryterium_zatrzymania):
    a = float(a)
    b = float(b)
    s = "Metoda bisekcji: "
    if funkcja(a) == 0:
        s += str(a)
        return s
    elif funkcja(b) == 0:
        s += str(b)
        return s

    elif funkcja(a) * funkcja(b) > 0:
        return "W danym przedziale nie ma miejsca zerowego"
    else:
        x1 = 0.0

        if 'liczba_operacji' in kryterium_zatrzymania:
            for i in range(int(kryterium_zatrzymania['liczba_operacji'])):
                x1 = (a + b) / 2.0
                if funkcja(x1) == 0:
                    s += str(x1)
                    return s
                if funkcja(a) * funkcja(x1) < 0:
                    b = x1
                else:
                    a = x1

        if 'dokladnosc' in kryterium_zatrzymania:
            while abs(funkcja(x1)) > float(kryterium_zatrzymania['dokladnosc']):
                x1 = (a + b) / 2.0
                if funkcja(x1) == 0:
                    s += str(x1)
                    return s
                if funkcja(a) * funkcja(x1) < 0:
                    b = x1
                else:
                    a = x1
        s += str(x1)
        return s


def oblicz_sieczne(funkcja, a, b, kryterium_zatrzymania):
    a = float(a)
    b = float(b)
    s = "Metoda siecznych: "
    if funkcja(a) == 0:
        s += str(a)
        return s
    elif funkcja(b) == 0:
        s += str(b)
        return s
    elif funkcja(a) * funkcja(b) > 0:
        pass # aby nie wyświetlało 2x informacji
    else:
        x1 = 0.0

#######################################
# GUI TOOLS
#######################################

questions = [
    inquirer.List(name='funkcja',
                  message="Którą funkcje wybierasz?",
                  choices=['wielomianowa', 'trygonometryczna', 'wykładnicza'],
                  ),
    inquirer.Text(name='przedzial_1',
                  message="Podaj początek przedziału: "
                  ),
    inquirer.Text(name='przedzial_2',
                  message="Podaj koniec przedziału: ",
                  ),
    inquirer.List(name='kryterium_zatrzymania',
                  message="Którą metodę zatrzymania wybierasz?",
                  choices=['dokładność obliczeń', 'osiągnięcie zadanej liczby operacji'],
                  ),

]
questions_kontynuowac = [
    inquirer.List(name='kontynuacja',
                  message="Kontynuować działanie programu?",
                  choices=['Tak', 'Nie']
                  ),
]

#######################################
# MAIN
#######################################
kontynuacja = True
while kontynuacja:
    answers = inquirer.prompt(questions)

    if answers['kryterium_zatrzymania'] == 'dokładność obliczeń':
        questions_kryterium_zatrzymania = [
            inquirer.Text(name='dokladnosc',
                          message="Podaj dokładność obliczeń: "
                          ),
        ]

    else:
        questions_kryterium_zatrzymania = [
            inquirer.Text(name='liczba_operacji',
                          message="Podaj ilość iteracji: "
                          ),
        ]

    answers_kryterium_zatrzymania = inquirer.prompt(questions_kryterium_zatrzymania)

    if answers['funkcja'] == 'wielomianowa':
        print(oblicz_bisekcja(funkcja_wielomianowa, answers['przedzial_1'], answers['przedzial_2'],
                              answers_kryterium_zatrzymania))

    elif answers['funkcja'] == 'trygonometryczna':
        oblicz_bisekcja(funkcja_trygonometryczna, answers['przedzial_1'], answers['przedzial_2'],
                        answers_kryterium_zatrzymania)
    elif answers['funkcja'] == 'wykladnicza':
        oblicz_bisekcja(funkcja_wykladnicza, answers['przedzial_1'], answers['przedzial_2'],
                        answers_kryterium_zatrzymania)

    answers_kontynuowac = inquirer.prompt(questions_kontynuowac)
    if answers_kontynuowac['kontynuacja'] == 'Nie':
        kontynuacja = False

    #######################
    # CLEAR
    #######################
    answers_kontynuowac.clear()
    answers.clear()
    answers_kryterium_zatrzymania.clear()
