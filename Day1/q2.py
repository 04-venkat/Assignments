import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 8) 
sales1 = [160, 150, 140, 145, 175, 165, 180] 
sales2 = [70, 90, 160, 150, 140, 145, 175] 
# plt.figure(figsize = (6, 5), dpi = 150)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.plot(days, sales1)
plt.plot(days, sales2)
plt.show()