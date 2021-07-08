import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from numpy.random import randn

fmri= sns.load_dataset('fmri')
fmri.head(10)

sns.relplot(x = 'timepoint', y = 'signal', data = fmri , hue = 'region', style = 'event')
plt.show()

sns.lineplot(x = 'timepoint', y = 'signal', data = fmri , hue = 'region', style = 'event')
plt.show()

sns.boxplot(x = "timepoint", y = "signal", data=fmri, hue = "event")
plt.show()