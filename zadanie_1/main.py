import inquirer
import time

print("----Zadanie 1 ----")


#######################################
# FUNCTION
#######################################

def funkcja_wielomianowa(x):
    return (x - 2) ** 2 - 3


def funkcja_trygonometryczna(x):
    pass


def funkcja_wykladnicza(x):
    pass


def oblicz_bisekcja(funkcja, a, b, kryterium_zatrzymania):
    a = float(a)
    b = float(b)

    if funkcja(a) == 0:
        print("Miejscem zerowym funkcji jest:", a)
    elif funkcja(b) == 0:
        print("Miejscem zerowym funkcji jest:", b)

    elif funkcja(a) * funkcja(b) > 0:
        print("W danym przedziale nie ma miejsca zerowego")
    else:
        x1 = 0.0

        if 'liczba_operacji' in kryterium_zatrzymania:
            for i in range(int(kryterium_zatrzymania['liczba_operacji'])):
                x1 = (a + b) / 2.0
                if funkcja(x1) == 0:
                    print("Miejscem zerowym jest:", x1)
                if funkcja(a) * funkcja(x1) < 0:
                    b = x1
                else:
                    a = x1

        if 'dokladnosc' in kryterium_zatrzymania:
            while abs(funkcja(x1)) > float(kryterium_zatrzymania['dokladnosc']):
                x1 = (a + b) / 2.0
                if funkcja(x1) == 0:
                    print("Miejscem zerowym jest:", x1)
                if funkcja(a) * funkcja(x1) < 0:
                    b = x1
                else:
                    a = x1
        print("Miejscem zerowym jest:", x1)


#######################################
# GIU TOOLS
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
questions_type = [
    inquirer.List(name='typ_obliczen',
                  message="Którą metodą chcez obliczyć?",
                  choices=['metoda bisekcji', 'metoda siecznych']
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

    # print(answers_kryterium_zatrzymania.keys())
    # time.sleep(1)
    # if answers_kryterium_zatrzymania.keys() == "dokladnosc":
    #     print("no dziala tu tez")
    #     time.sleep(10)
    answers_type = inquirer.prompt(questions_type)

    if answers_type['typ_obliczen'] == 'metoda bisekcji':
        if answers['funkcja'] == 'wielomianowa':
            oblicz_bisekcja(funkcja_wielomianowa, answers['przedzial_1'], answers['przedzial_2'],
                            answers_kryterium_zatrzymania)

        elif answers['funkcja'] == 'trygonometryczna':
            oblicz_bisekcja(funkcja_trygonometryczna, answers['przedzial_1'], answers['przedzial_2'],
                            answers_kryterium_zatrzymania)
        elif answers['funkcja'] == 'wykladnicza':
            oblicz_bisekcja(funkcja_wykladnicza, answers['przedzial_1'], answers['przedzial_2'],
                            answers_kryterium_zatrzymania)

    answers_kontynuowac = inquirer.prompt(questions_kontynuowac)
    if answers_kontynuowac['kontynuacja'] == 'Nie':
        kontynuacja = False
    answers_kontynuowac.clear()
    answers.clear()
    answers_kryterium_zatrzymania.clear()


