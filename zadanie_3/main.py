import menu
import logika


*data, nodes = menu.menu()

nodes_values = logika.get_nodes_values(nodes, data[1])

newton = logika.get_all_results(data[0], nodes_values, nodes, logika.newton_interpolation)

menu.wyswietl_wykres(data[0], data[1], nodes, nodes_values, newton)
