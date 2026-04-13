import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 6)
y1 = x * 2
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Line Graph")
y2 = [5, 7, 3, 8, 6]
plt.subplot(2, 2, 2)
plt.bar(x, y2)
plt.title("Bar Graph")
y3 = [2, 9, 4, 7, 1]
plt.subplot(2, 2, 3)
plt.scatter(x, y3)
plt.title("Scatter Plot")
plt.show()