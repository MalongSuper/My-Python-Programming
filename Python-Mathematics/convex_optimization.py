# Convex Optimization
import numpy as np
import matplotlib.pyplot as plt


def is_convex_function(f, x1, x2, iterations=100, tolerance=1e-9):
    # Lambda is always between 0 and 1
    lambdas = np.linspace(0, 1, iterations)
    for lamb in lambdas:
        f_left = f(lamb * x1 + (1 - lamb) * x2)
        f_right = lamb * f(x1) + (1 - lamb) * f(x2)
        # If this condition breaks the loop, then the function is not convex
        if f_left > f_right + tolerance:  # Add a tolerance
            return False
    return True


def plot_function(f_input):
    # Plot the function
    x_values = np.linspace(x1, x2, 400)
    y_values = f(x_values)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f_input)
    # Draw axes through origin
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.title(f'Plot of the Function: {f_input}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()


# The main function
print("Convex Optimization")
f_input = input("Enter equation f(x): ").replace("^", "**")
f = eval(f"lambda x: {f_input}", {"np": np})
x1, x2 = eval(input("Enter x1, x2: "))
plot_function(f_input)
# Check for convexity
if is_convex_function(f, x1, x2):
    print(f"The function is convex with x1 = {x1}; x2 = {x2}")
else:
    print("The function is not convex")
