# Gradient Descent
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def derivative(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    return sp.diff(fx, x)


def plot_function(f_input):
    # Plot the function
    x_values = np.linspace(-10, 10, 400)
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


# Gradient Descent is an iterative optimization algorithm
# that aims to estimate where a differentiable function produce its lowest values.
def gradient_descent(x0, f, df, learning_rate, iterations=20):
    # Run Gradient Descent
    x_gd = [x0]
    # Obtain all the x values
    for _ in range(iterations):
        x_new = x_gd[-1] - learning_rate * df(x_gd[-1])
        x_gd.append(x_new)
    # Read as array then substitute to the function
    x_gd = np.array(x_gd)
    y_gd = f(x_gd)
    # Print the results
    for i in range(len(x_gd)):
        print(f"At x = {x_gd[i]}, y = {y_gd[i]}")


# Example output: (x**2 * np.cos(x) - x) / 10
f_input = input("Enter equation f(x): ").replace("^", "**")
f = eval(f"lambda x: {f_input}", {"np": np})
df_expr = derivative(f_input.replace("np.", ""))
# Convert symbolic derivative to NumPy function
x_sym = sp.symbols('x')
df = sp.lambdify(x_sym, df_expr, modules="numpy")
# Set a starting x
x0 = float(input("Enter x0: "))
print("Gradient Descent:")
gradient_descent(x0, f, df, 0.1, 20)

# Plot function
plot_function(f_input)
