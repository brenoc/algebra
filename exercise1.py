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

a, b, c, d = np.linalg.lstsq(A, b)[0]


print "System solution:"
print [a, b, c, d]

x = [0, 1, 2, 4]
plt.plot(p1, p2, p3, p4, 'o', label='Original data', markersize=10)
# plt.plot(1, a*1**3+b*1**2+c*1+d, 'r', label='Fitted line')
plt.show()
