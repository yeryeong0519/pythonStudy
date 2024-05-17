import matplotlib.pyplot as plt
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['봄', '여름', '가을', '겨울']
plt.title("계절별 서울 온도")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)
plt.yticks(sorted(temperatures))
plt.show()