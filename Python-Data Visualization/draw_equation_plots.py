import matplotlib.pyplot as plt
import numpy as np


# Draw the graph of a mathematical expression
def plot_equation(equation, x_label, y_label, title,
                  x_min=-10, x_max=10):

    x = np.linspace(x_min, x_max, 1000)
    y = eval(equation)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=equation, linewidth=2)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.axhline(0, linestyle='--')
    plt.axvline(0, linestyle='--')
    plt.grid(True)
    plt.legend()

    plt.show()


# Convert user-friendly math syntax into NumPy syntax
def preprocess(expr):
    expr = expr.replace("^", "**")

    replacements = {"sin(": "np.sin(",
                    "cos(": "np.cos(",
                    "tan(": "np.tan(",
                    "exp(": "np.exp(",
                    "log(": "np.log(",
                    "sqrt(": "np.sqrt(",
                    "pi": "np.pi"}

    for old, new in replacements.items():
        expr = expr.replace(old, new)

    return expr


# Read an equation from the user and plot it
def main():
    expression = input("Enter f(x): ")
    expression = preprocess(expression)

    plot_equation(expression, "x","f(x)",f"Plot of {expression}")


# Start the program
if __name__ == "__main__":
    main()
