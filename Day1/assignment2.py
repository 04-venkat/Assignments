import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)
y = [160, 150, 140, 145, 175, 165, 180]
plt.plot(x, y)
plt.xlabel("Days", color="b")
plt.ylabel("Sales", color="b")
plt.show()

days = np.arange(1, 8) 
sales1 = [160, 150, 140, 145, 175, 165, 180] 
sales2 = [70, 90, 160, 150, 140, 145, 175] 
# plt.figure(figsize = (6, 5), dpi = 150)
plt.subplot(1, 2, 1)
plt.xlabel("Days", color="b")
plt.ylabel("Sales", color="b")
plt.plot(days, sales1)
plt.subplot(1, 2, 2)
plt.xlabel("Days", color="b")
plt.ylabel("Sales", color="b")
plt.plot(days, sales2)
plt.show()