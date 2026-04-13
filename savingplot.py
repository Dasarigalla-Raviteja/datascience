import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.plot(x, y, linestyle='--', marker='o')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine Wave Plot")
plt.grid(True)
plt.savefig("sine_plot.png")      
plt.savefig("sine_plot.pdf")      
plt.savefig("sine_plot.jpg")      

plt.show()