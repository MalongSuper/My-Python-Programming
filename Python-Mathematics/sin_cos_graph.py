# Draw Graph of sin(x) and cos(x)
import numpy as np
import matplotlib.pyplot as plt
# Function for Graph
x = np.arange(0.0, 4 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# Plotting Graph
plt.title("Graph of sin(x) and cos(x)")
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="blue")
plt.grid()
# Display Graph
plt.show()
