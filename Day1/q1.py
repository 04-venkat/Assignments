import numpy
import matplotlib.pyplot as plt

a = numpy.arange(40,50)
b = numpy.arange(50,60)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(a, b)
plt.show()