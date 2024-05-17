import numpy as np
a = np.array([1, 2, 3])
t = a + 1
print(t)
x = np.array([4, 8, 12])
y = np.array([2, 4, 6])
z = x / y
print(z)
k = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
m = np.array([2, 3, 4], [5, 6, 7], [8, 9, 10])
print(k[1])
print(k[:,1])
print(k[:,1]+m[:,1])
b = np.array([10, 20, 30, 40, 50, 60, 70])