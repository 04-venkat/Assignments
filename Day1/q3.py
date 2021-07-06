import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

plt.subplot(3, 3, 1)
plt.plot(x, y1, 'r')
plt.subplot(3, 3, 2)
plt.plot(x, y2, 'r--')
plt.subplot(3, 3, 3)
plt.plot(x, y3, 'b')
plt.subplot(3, 3, 4)
plt.plot(x, y4, 'b--')
plt.subplot(3, 3, 5)
plt.plot(x, y5)
plt.show()