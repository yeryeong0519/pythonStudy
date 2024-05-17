import numpy as np

a = np.linspace(0, 12, 4)
print(a)
b = np.linspace(0, 12, 4, retstep = True)
print(b)
c = np.linspace(0, 12, 3, endpoint = False)
print(c)