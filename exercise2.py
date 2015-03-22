import numpy as np

a = np.array([
    [1, -1, 1],
    [0, 1, 1],
    [1, 0, 2]])

ainv = np.linalg.inv(a)

print ainv
