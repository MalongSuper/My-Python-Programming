# Finite difference of Cosine function
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x)


def main():
    print("Finite difference of Cosine function")
    # Get user input for the range and step size
    start = float(input("Enter the start of the range: "))
    end = float(input("Enter the end of the range: "))
    step = float(input("Enter the step size: "))

    # Create the x values based on user input
    x = np.arange(start, end, step)
    h = step  # Use the same step size for finite difference

    # Calculate the derivative using Finite Difference
    y_derivative = (f(x + h) - f(x - h)) / (2 * h)

    # Calculate the exact derivative
    y_derivative_exact = -np.sin(x)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_derivative, 'r--', label='Finite Difference Approximation', color='red')
    plt.plot(x, y_derivative_exact, label='Exact Derivative: -sin(x)', color='blue')
    plt.title('Derivative of f(x) = cos(x)')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.legend()
    plt.grid()
    plt.show()


main()
