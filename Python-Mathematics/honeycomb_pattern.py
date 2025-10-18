# Honeycomb pattern plot
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
y = np.random.randn(10000)

# Figure 1: cmap = "plasma"
plt.hexbin(x, y, gridsize=30, cmap='plasma', edgecolor='gray')
plt.colorbar(label='Count in bin')
plt.title("Honeycomb Pattern Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Figure 2: cmap = "Blues"
plt.hexbin(x, y, gridsize=30, cmap='Blues', edgecolor='gray')
plt.colorbar(label='Count in bin')
plt.title("Honeycomb Pattern Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Figure 3: cmap = "Greens"
plt.hexbin(x, y, gridsize=30, cmap='Greens', edgecolor='gray')
plt.colorbar(label='Count in bin')
plt.title("Honeycomb Pattern Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Figure 4: cmap = "Reds"
plt.hexbin(x, y, gridsize=30, cmap='Reds', edgecolor='gray')
plt.colorbar(label='Count in bin')
plt.title("Honeycomb Pattern Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
