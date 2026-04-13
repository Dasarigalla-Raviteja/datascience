import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.plot(x, [10, 20, 25, 30], label="Growth")
plt.plot(x, [30, 25, 20, 15], label="Decline")
plt.legend(loc='upper left')  
plt.show()