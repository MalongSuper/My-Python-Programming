# Pattern Classification
from ortools.linear_solver import pywraplp
import numpy as np
import matplotlib.pyplot as plt


# Given A is a set of data in a hyperplane
# So that a0 * x0 + a1 * x1 + ... + a(n - 1) * x(n - 1) - an > 0
# B is opposite with A. Thus, when testing the sample data
# if finding a value > 0 then it belongs to A
def solve_binary_classification(a, b):
    n = len(a[0])  # Decisive constants
    ma, mb = len(a), len(b)
    a_min, a_max = -99, 99
    s = pywraplp.Solver('Binary pattern classification',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decisive constants. Note that the upper limit, lower limit remain unchanged
    # vector A in range -99 and 99 can produce inaccurate result, but it is fast
    ya = [s.NumVar(0, a_max, '') for _ in range(ma)]
    yb = [s.NumVar(0, a_max, '') for _ in range(mb)]
    # Note that vector A has one more element at the end is "An"
    # Then it has (n + 1) elements
    vect_a = [s.NumVar(a_min, a_max, '') for _ in range(n + 1)]
    # Constraints. Note that a[n] is a0
    k = 1  # The minimum distance from each point to the hyperplane
    for i in range(ma):
        s.Add(ya[i] >= vect_a[n] + k - s.Sum(vect_a[j] * a[i][j] for j in range(n)))
    for i in range(mb):
        s.Add(yb[i] >= s.Sum(vect_a[j] * b[i][j] for j in range(n)) - vect_a[n] + k)
    # Objective function
    a_gap = s.Sum(ya[i] for i in range(ma))
    b_gap = s.Sum(yb[i] for i in range(mb))
    s.Minimize(a_gap + b_gap)
    status = s.Solve()
    obj_val = s.Objective().Value()
    sol_val = [v.solution_value() for v in vect_a]
    return status, obj_val, sol_val


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
    status, obj_val, sol_val = solve_binary_classification(A, B)
    print("Status =", status)
    print('Objective value =', obj_val)
    print('Solution =', sol_val)
    # Draw a plot of data points and dividing lines
    A = np.array(A)
    B = np.array(B)
    # Setting x-axis and y_axis limits
    plt.title("Pattern Classification (Binary)")
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
