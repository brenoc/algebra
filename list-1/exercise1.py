import numpy as np
import matplotlib.pyplot as plt

p1 = [0, 1]
p2 = [1, 0]
p3 = [2, -1]
p4 = [3, 2]

e1 = [1, 1, 1, 1]
e2 = [8, 4, 2, 1]
e3 = [27, 9, 3, 1]
e4 = [0, 0, 0, 1]

A = np.array([e1, e2, e3, e4])
b = np.array([0, -1, 2, 1])

a, b, c, d = np.linalg.solve(A, b)

print "System solution:"
print [a, b, c, d]

x = np.arange(-3, 5, 0.25)

px = [0, 1, 2, 3]
py = [1, 0, -1, 2]

F = a*x**3+b*x**2+c*x*1+d

plt.plot(x, F, 'r', label='Fitted line')
plt.plot(px, py, 'o', label='Original data', markersize=4)
plt.legend()
plt.show()
