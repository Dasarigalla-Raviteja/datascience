import matplotlib.pyplot as plt
import numpy as np


fig, axs = plt.subplots(2, 2)
x = np.linspace(0, 10, 100)
y = np.sin(x)
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Sine Wave")
y2 = np.cos(x)
axs[0, 1].scatter(x, y2)
axs[0, 1].set_title("Cosine Scatter")
categories = ["A", "B", "C", "D"]
values = [15, 25, 10, 20]
axs[1, 0].bar(categories, values)
axs[1, 0].set_title("Bar Chart")
data = np.random.randn(100)
axs[1, 1].hist(data)
axs[1, 1].set_title("Histogram")
plt.tight_layout()
plt.show()