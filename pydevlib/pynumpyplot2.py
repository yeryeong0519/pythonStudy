#numpy를 이용한 plot 기능
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 10)
y = x**2
plt.plot(x, y)
plt.show()