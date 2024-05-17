import matplotlib.pyplot as plt
# y = [1, 2, 3, 4, 5]
x = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
y1 = [13, 16, 15, 18, 16, 17, 16]
y2 = [20, 23, 22, 25, 22, 20, 18]
plt.title("5월 3째주 기온변화")
plt.xlabel("요일")
plt.ylabel("온도")
plt.plot(x, y1, label = 'lowest temperature')
plt.plot(x, y2, label = 'highest temparature')
plt.legend(loc = "upper left")
plt.show()