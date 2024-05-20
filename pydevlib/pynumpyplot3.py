#numpy를 이용한 plot 기능
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth = 2, markersize = 12, label = "First")
plt.plot(x, y2, "gs-", linewidth = 3, markersize = 5, label = "Second")
plt.legend(loc = "uppser left")
plt.show()