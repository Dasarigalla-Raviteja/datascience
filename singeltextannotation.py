import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = x * 3
plt.plot(x, y, marker='o')
plt.annotate("Highest Value",
             xy=(5, 15),        # point
             xytext=(3, 12),    # text position
             arrowprops=dict(arrowstyle='->', color='black'),
             bbox=dict(boxstyle="round", fc="yellow"))
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Text Annotation Example")
plt.grid(True)
plt.show()