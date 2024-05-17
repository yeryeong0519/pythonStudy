import matplotlib.pyplot as plt
f = lambda x:x**2
x = [x for x in range (-8, 9)]
y = [f(y) for y in range(-8, 9)]
print(x)
print(y)
plt.plot(x, y)
plt.show()