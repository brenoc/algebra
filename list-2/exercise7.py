# O arquivo MatrizIncidencia.csv que acompanha esta lista contem a matriz de
# incidencia de uma rede direcionada (grafo), onde cada linha representa uma
# aresta e cada coluna um vertice. Se Aij = 1 entao a aresta i se inicia no
# vertice j. Se Aij = -1 entao a aresta i termina no vertice j. Deste modo em
# cada linha i ha apenas uma entrada igual a 1 e uma entrada igual a -1 e todos
# demais elementos desta linha sao iguais a zero.

# a) Encontre uma base para o nucleo da matriz de incidencia. Voce pode usar um
# pacote computacional, claro!

# b) Descreva quantas componentes conexas esta rede possui e quais sao os
# vertices que pertencem a cada componente.

import csv
import networkx as nx
import matplotlib.pyplot as plt


def read_matrix_file(file_name):
    rows = []
    with open(file_name, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            rows.append(row)

    return rows


def create_graph(edges):
    G = nx.Graph()
    for edge in edges:
        from_node = None
        to_node = None
        for node, col in enumerate(edge):
            if int(col) is 1:
                from_node = node
            elif int(col) is -1:
                to_node = node
        G.add_edge(from_node, to_node)
    return G


def print_graph(graph):
    pos = nx.graphviz_layout(graph, prog="neato")
    nx.draw(graph, pos)
    plt.show()

if __name__ == '__main__':
    edges = read_matrix_file('MatrizIncidencia.csv')
    graph = create_graph(edges)
    print_graph(graph)
