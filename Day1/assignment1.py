import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
plt.title("sine")
plt.xlabel("Integer", color="b")
plt.ylabel("Square", color="r")
plt.plot(x, y, color='r')
plt.show()