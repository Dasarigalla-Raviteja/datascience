import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 6)
y = [5, 15, 25, 35, 45]
plt.plot(x, y)
plt.xlabel("Time (seconds)", fontsize=12)
plt.ylabel("Value Growth", fontsize=12)
plt.title("Sample Line Graph")
plt.grid(True)
plt.show()