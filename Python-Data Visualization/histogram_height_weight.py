# Histogram with Python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

df = pd.read_csv('datasets/SOCR-HeightWeight.csv').drop(columns='Index')

# Draw the histogram
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].hist(df['Height(Inches)'], bins=30, color='lightcoral', edgecolor='black')
axs[0].set_title('Height(Inches)')
axs[1].hist(df['Weight(Pounds)'], bins=30, color='lightblue', edgecolor='black')
axs[1].set_title('Weight(Pounds)')
# Add labels and title
# Increase the gap between the two plots
plt.subplots_adjust(wspace=0.4)
plt.suptitle('SOCR-Height Weight Distribution')
plt.show()
