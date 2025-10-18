# Pattern Classification Revisited: Executable model
# with maximizing the margin
from ortools.linear_solver import pywraplp
import numpy as np
import matplotlib.pyplot as plt


def solve_margins_classification(class_a, class_b):
    n = len(class_a[0])
    ma, mb = len(class_a), len(class_b)
    s = pywraplp.Solver('Classification with maximizing the margin',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables
    ua = [s.NumVar(0, 99, '') for _ in range(ma)]
    la = [s.NumVar(0, 99, '') for _ in range(ma)]
    ub = [s.NumVar(0, 99, '') for _ in range(mb)]
    lb = [s.NumVar(0, 99, '') for _ in range(mb)]
    a = [s.NumVar(-99, 99, '') for _ in range(n + 1)]
    e = s.NumVar(0, 99, 'e')
    # Constraints, note: a[n] is a0 in the lesson
    # a0 * x0 + a1 * x1 + ... = an
    for i in range(ma):
        # Constraints to force the data point x belongs to A
        s.Add(0 >= a[n] + 1 - s.Sum(a[j] * class_a[i][j] for j in range(n)))
        # Constraints to force the data point x belongs to hyperplane
        s.Add(a[n] == s.Sum(a[j] * class_a[i][j] - ua[i] + la[i] for j in range(n)))
        # e is the lower border of u, l
        s.Add(ua[i] >= e)
        s.Add(la[i] >= e)
    for i in range(mb):
        s.Add(0 >= s.Sum(a[j] * class_b[i][j] for j in range(n)) - a[n] + 1)
        s.Add(a[n] == s.Sum(a[j] * class_b[i][j] - ub[i] + lb[i] for j in range(n)))
        s.Add(ub[i] >= e)
        s.Add(lb[i] >= e)
    s.Minimize(e)
    status = s.Solve()
    sol_val = [v.solution_value() for v in a]
    return status, sol_val


def main():
    # Sets of A, B
    # A = [[1, 2], [2, 4], [4, 9], [5, 6]
    # B = [[4, 1], [5, 2], [6, 4], [8, 9]
    # Suppose a sample set of data
    means = [[2, 4], [5, 3]]
    cov = np.array([[0.6, 0.2], [0.2, 0.6]])  # Covariance matrix
    N = 100
    np.random.seed(7)  # Similar random set of data in each run
    A = np.random.multivariate_normal(means[0], cov, N)
    B = np.random.multivariate_normal(means[1], cov, N)
    status, sol_val = solve_margins_classification(A, B)
    print("Status =", status)
    print('Solution =', sol_val)
    # Draw a plot of data points and dividing lines
    A = np.array(A)
    B = np.array(B)
    # Setting x-axis and y_axis limits
    plt.title("Pattern Classification (Margins)")
    plt.xlim(0, 10), plt.ylim(0, 10)
    plt.scatter(A[:, 0], A[:, 1], marker='o', color='blue')
    plt.scatter(B[:, 0], B[:, 1], marker='x', color='red')
    a = sol_val
    x = np.linspace(0, 10, 100)
    # Since the initial hyperplane equation has form: a[0] * x0 + a[1] * x1 = a[2]
    # [x0, x1] corresponds to value (x, y) of equation y = ax + b
    y = (a[2] - a[0] * x) / a[1]
    plt.plot(x, y, color='green')
    plt.show()


main()
