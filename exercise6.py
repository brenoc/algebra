L = [
    [1, 0, 0],
    [2, 1, 0],
    [1, 1, 2]
    ]

b = [3,
     2,
     1]

# L * x = b
# L is a lower triangular matrix (nxn) 
# x is a vector (nx1)
# b is a vector (nx1)

def solve(matrix, vector):
    solution = []
    for i, row in enumerate(matrix):
        if i is 0:
            solution.append(vector[0] / matrix[0][0])
        else:
            temp = 0
            for j, col in enumerate(row):                
                if j < i:
                    temp = temp + solution[j] * matrix[i][j]
                elif j is i:
                    right_side = vector[j] - temp
                    solution.append(right_side / matrix[i][j]) 

    return solution


if __name__ == '__main__':
    solution = solve(L, b)

    print solution
