from matplotlib import pyplot as plt
import numpy as np
import logika
import inquirer


def get_function():
    in_number = ''
    question = [inquirer.List(name='funkcja', message="Wybierz wzór funkcji", choices=['2 * x - 9',
                                                                                       '3 * x ** 3 - 5',
                                                                                       'np.sin(x ** 2) - np.cos(x)',
                                                                                       '5*np.absolute(np.sin(x)-2)'])]
    answer = inquirer.prompt(question)
    if answer['funkcja'] == '2 * x - 9':
        in_number = '1'
    elif answer['funkcja'] == '3 * x ** 3 - 5':
        in_number = '2'
    elif answer['funkcja'] == 'np.sin(x ** 2) - np.cos(x)':
        in_number = '3'
    else:
        in_number = '4'

    return in_number


def get_zakres():
    questions = [inquirer.Text(name='a', message='Podaj początek przedzialu'),
                 inquirer.Text(name='b', message='Podaj koniec przedzialu')]
    answers = inquirer.prompt(questions)

    return float(answers['a']), float(answers['b'])


def get_ilosc_wezlow():
    question = [inquirer.Text(name='wezly', message='Podaj ilość węzłów')]
    answer = inquirer.prompt(question)
    return int(answer['wezly'])


def menu():
    formula = get_function()
    formula_range = get_zakres()
    choice = wybor_wezlow()
    if choice == '1':
        nodes_number = get_ilosc_wezlow()
        nodes = tworzenie_wezlow_rownoodleglych(nodes_number, formula_range)
    else:
        nodes = wezly_z_pliku(formula_range)
        if not nodes:
            print('Nieprawidlowe dane w pliku. Trwa losowanie')
            nodes_number = get_ilosc_wezlow()
            nodes = tworzenie_wezlow_rownoodleglych(nodes_number, formula_range)
    checked_formula = wybor_funkcji(formula)
    return [formula_range, checked_formula, nodes]


def wybor_funkcji(in_number):
    switcher = {
        '1': '2 * x - 9',
        '2': '3 * x ** 3 - 5',
        '3': 'np.sin(x ** 2) - np.cos(x)',
        '4': '5*np.absolute(np.sin(x)-2)'
    }
    return switcher.get(in_number, 'invalid input')


def wybor_wezlow():
    choice = ''
    questions = [inquirer.List(name='wezel', choices=['węzły równoodległe', 'wczytaj węzły z pliku'])]
    answers = inquirer.prompt(questions)
    if answers['wezel'] == 'węzły równoodległe':
        choice = '1'
    else:
        choice = '2'

    return choice


def wezly_z_pliku(formula_range):
    nodes = np.genfromtxt(fname='nodes.txt', delimiter=",")

    return walidator(formula_range, nodes)


def tworzenie_wezlow_rownoodleglych(nodes_number, formula_range):  # tworzenie węzłów równoodległych
    nodes = np.linspace(formula_range[0], formula_range[1], nodes_number)
    # nodes = np.sort(nodes)
    return np.array(nodes)


def walidator(formula_range, nodes):  # sprawdza, czy dane w nodes.txt są prawidłowe
    valid_nodes = [element for element in nodes if formula_range[0] <= element < formula_range[1]]
    return valid_nodes


def wykres(formula_range, formula):
    x = np.linspace(formula_range[0], formula_range[1])
    y = []
    for i in range(len(x)):
        y.append(logika.get_fun_value(formula, x[i]))
    plt.plot(x, np.array(y), label='Wykres funkcji')


def wyswietl_wykres(formula_range, formula, nodes, nodes_values, newton):
    wykres(formula_range, formula)
    plt.plot(newton[0], newton[1], '*', zorder=0, linewidth=4,
             label='Wykres wielomianu interpolacyjnego metody Newtona')
    plt.scatter(nodes, np.array(nodes_values), label='Węzły interpolacyjne')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')
    plt.savefig('wykres.png',
                dpi=300,
                format='png',
                bbox_inches='tight')
    plt.show()
