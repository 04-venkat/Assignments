import matplotlib.pyplot as plt
import seaborn as sns

fmri= sns.load_dataset('fmri')
fmri.head(10)

sns.relplot(x = 'timepoint', y = 'signal', data = fmri , hue = 'region', style = 'event')
plt.show()

sns.lineplot(x = 'timepoint', y = 'signal', data = fmri , hue = 'region', style = 'event')
plt.show()

sns.boxplot(x = "timepoint", y = "signal", data=fmri, hue = "event")
plt.show()
