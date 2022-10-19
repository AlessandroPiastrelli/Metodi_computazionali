import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('vel_vs_time.csv')
df

plt.rcParams["figure.figsize"] = [10, 4.5]
plt.rcParams["figure.autolayout"] = True

x = df['t']
y = df['v']

plt.plot(x,y)
plt.xlabel('Tempo')
plt.ylabel('Velocità')
plt.show()

