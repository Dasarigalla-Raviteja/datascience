import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xticks([1, 2, 3, 4], ['One', 'Two', 'Three', 'Four'], rotation=45)
plt.show()