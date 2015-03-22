import numpy as np

L = [
    [1, 0, 0],
    [2, 1, 0],
    [1, 1, 2]
    ]

b = [3,
     2,
     1]

# L * x = b
# L is a matrix (nxn)
# x is a vector (nx1)
# b is a vector (nx1)


def eliminate(matrix, vector, i, j):
    mult = matrix[i][j] / matrix[j][j]
    row_mult = map(lambda x: x*mult, matrix[j])
    matrix[i] = map(lambda x, y: x - y, matrix[i], row_mult)
    vector[i] = vector[i] - mult * vector[j]
    return matrix, vector


def multiply_matrix_by_vector(matrix, vector):
    for i, row in enumerate(matrix):
        if i > 0 and i != len(matrix):
            for j, col in enumerate(row):
                if j < i and matrix[i][j] != 0:
                    matrix, vector = eliminate(matrix, vector, i, j)

    return matrix, vector


if __name__ == '__main__':
    matrix, vector = multiply_matrix_by_vector(L, b)

    print matrix
    print vector
