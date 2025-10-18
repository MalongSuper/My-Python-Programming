# Linear Regression
import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, y):
    n = len(x)
    x_mean = np.sum(x) / n
    y_mean = np.sum(y) / n
    # Compute the values of linear equation y = b*x + a
    # Use the complete formula
    a = ((y_mean * np.sum(x * x) - x_mean * np.sum(x * y)) /
         (np.sum(x * x) - n * x_mean ** 2))
    b = np.sum(y * (x - x_mean)) / np.sum(x * (x - x_mean))
    # Compute b first, then compute a based on Mean
    # b = np.sum(y * (x - x_mean)) / np.sum(x * (x - x_mean))
    # a = y_mean - b * x_mean
    coefficient = np.array([b, a])
    return coefficient


def main():
    n = 50
    x = np.linspace(1, 20, n)
    print("Linear Regression")
    a, b = eval(input("Enter a, b: "))
    y = b * x + a + (np.random.randn(n) * 0.9)
    coefficient = linear_regression(x, y)
    y_new = x * coefficient[0] + coefficient[1]

    # Draw points (x, y)
    plt.scatter(x, y, marker='.')
    # Draw regression line
    plt.plot(x, y_new, color='red')
    plt.title(f"y = ({coefficient[0]: .3f}) * x + ({coefficient[1]: .3f})")
    plt.show()


main()
