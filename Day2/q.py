import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(10, 4), columns = ['a', 'b', 'c', 'd'])

df.plot(kind = "bar")
plt.title("Randomized Bar Graph")
plt.show()