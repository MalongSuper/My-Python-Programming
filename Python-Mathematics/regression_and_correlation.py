# Regression and Correlation in Statistics
import matplotlib.pyplot as plt


def find_regression(matrix, x, y):
    n = len(matrix)
    # Find the required values
    total_x = sum(x)
    total_y = sum(y)
    total_xy = sum([x[i] * y[i] for i in range(len(x))])
    total_squared_x = sum([x[i] ** 2 for i in range(len(x))])
    total_x_squared = sum(x) ** 2
    # Calculate B using the Regression formula
    b = (((n * total_xy) - (total_x * total_y)) /
         (n * total_squared_x - total_x_squared))
    a = (total_y - b * total_x) / n
    return a, b


def find_correlation(matrix, x, y):
    n = len(matrix)
    # Find the required values
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    total_xy = sum([x[i] * y[i] for i in range(len(x))])
    total_squared_x = sum([x[i] ** 2 for i in range(len(x))])
    total_squared_y = sum([y[i] ** 2 for i in range(len(y))])
    r = ((total_xy - n * mean_x * mean_y) /
         ((total_squared_x - n * (mean_x ** 2)) ** 0.5
          * (total_squared_y - n * (mean_y ** 2)) ** 0.5))
    return r


def main():
    print("Regression and Correlation")
    # A 2D Array (Matrix) that stores the statistical table
    M = []
    number = int(input("Enter the length of the table: "))
    for k in range(number):
        Xi, Yi = eval(input(f"Enter X{k + 1} and Y{k + 1}: "))
        M.append([Xi, Yi])  # Append tp list
    # X: The first column, Y: The second column
    X = [M[i][0] for i in range(len(M))]
    Y = [M[i][1] for i in range(len(M))]
    A, B = find_regression(M, X, Y)
    print(f"The Regression equation: Y = {A} + {B}X")
    R = find_correlation(M, X, Y)
    print(f"Correlation of X, Y: {R}")
    # Plot the data points (scatter plot)
    plt.scatter(X, Y, color='blue', label='Data Points')
    # Plot the regression line
    regression_line = [A + B * x_val for x_val in X]
    plt.plot(X, regression_line, color='red', label=f'Y = {A: .2f} + {B: .2f}X')
    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression: Scatter Plot and Regression Line')
    plt.legend()
    # Show the plot
    plt.show()


main()
