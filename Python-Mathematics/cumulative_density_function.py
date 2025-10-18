# Probability and Statistics problem
# Find Normal Cumulative Density Function (Normal CD or CDF)
# Use numerical integration
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt


def f(y):  # The formula for finding cdf
    return (1 / (sqrt(2 * pi))) * np.exp(-y ** 2 / 2)


def cumulative_density(x):
    lower = -10  # Very small number leads to inaccurate result
    upper = x
    val = np.linspace(upper, lower, 1000)
    I_trapezoids = np.trapz(f(val), val)
    res = abs(I_trapezoids)
    return res


def main():
    x = float(input("Enter x: "))
    result = cumulative_density(x)
    print(f"CDF value at x = {x} is {result}")
    # Plotting the bell curve (PDF)
    x_values = np.linspace(-5, 5, 1000)
    pdf_values = f(x_values)
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, pdf_values, label="Normal Distribution PDF")
    plt.fill_between(x_values, 0, pdf_values,
                     where=(x_values <= x), color="skyblue", alpha=0.4, label=f"CDF at x={x: .2f}")
    plt.axvline(x, color='r', linestyle='--', label=f"x = {x}")
    plt.title("Standard Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


# Avoid running the main function
# when importing the 'module' to another program
if __name__ == "__main__":
    main()
