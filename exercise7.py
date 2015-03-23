import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from math import log

# Estime a complexidade do algoritmo de solucao de sistemas lineares do pacote
# computacional de sua preferencia: registre os tempos que o pacote levou para
# resolver sistemas aleatorios n x n, com n = 16, 32, 64, 128, 256, 512, 1024,
# 2048. Faca um grafico do log do numero de colunas contra o log dos tempos
# registrados. O algoritmo do pacote tem complexidade inferior a O(n3)?


def generate_equation(n):
    eq = []
    for i in range(0, n):
        eq.append(random.randint(1, 20))

    return eq


def generate_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append(generate_equation(n))

    return matrix


def solve_system(matrix, vector):
    A = np.array(matrix)
    b = np.array(vector)

    return np.linalg.solve(A, b)


def run_scenario(n):
    matrix = generate_matrix(n)
    vector = generate_equation(n)

    return solve_system(matrix, vector)


def time_scenario(n):

    start = time.time()
    run_scenario(n)
    end = time.time()

    elapsed = end - start

    return elapsed


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = sys.argv[1]
        print "Elapsed time for solving matrix "+n+"x"+n+":"
        print time_scenario(int(n))
    else:
        n_array = [16, 32, 64, 128, 256, 512, 1024, 2048]
        time_array = []
        for n in n_array:
            print "Elapsed time for solving matrix "+str(n)+"x"+str(n)+":"
            elapsed = time_scenario(n)
            print elapsed
            time_array.append(elapsed)

        plt.plot(map(lambda x: log(x), n_array), map(lambda x: log(x), time_array))
        plt.show()
