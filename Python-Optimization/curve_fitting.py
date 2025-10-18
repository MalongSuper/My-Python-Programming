# Polynomial Curve Fitting Model
# Use Linear Programming to solve
# Find the polynomial function of order n equivalent to the set of data
from ortools.linear_solver import pywraplp
import matplotlib.pyplot as plt
import numpy as np


def solve_curve_fitting(d, degree=1, objective=0):
    s = pywraplp.Solver('Polynomial Curve Fitting',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(d)
    b = s.infinity()  # bound (the limit of the boundary value)
    # Decision variables for coefficient a
    # Number of coefficients a = the order of polynomial + 1 (since there is a0)
    a = [s.NumVar(-b, b, 'a[%i]' % i) for i in range(degree + 1)]
    # Substitute variables u, v
    u = [s.NumVar(0.0, b, 'u[%i]' % i) for i in range(n)]
    v = [s.NumVar(0.0, b, 'v[%i]' % i) for i in range(n)]
    # Maximize variable of the deviation
    e = s.NumVar(0.0, b, 'e')
    # Constraints
    for i in range(n):
        s.Add(u[i] - v[i] == d[i][1] - sum(a[j] * d[i][0] ** j
                                           for j in range(degree + 1)))
    for i in range(n):
        s.Add(u[i] <= e)
        s.Add(v[i] <= e)
    # Objective function (for 2 approaches using absolute value or min-max
    if objective == 0:  # sum fit
        cost = sum(u[i] + v[i] for i in range(n))
    else:  # max fit
        cost = e
    s.Minimize(cost)
    status = s.Solve()
    obj_val = s.Objective().Value()
    sol_val = [a.solution_value() for a in a]
    return status, obj_val, sol_val


def main():
    D = [[0.1584, 0.0946],
         [0.8454, 0.2689],
         [2.1017, 5.8285],
         [3.1966, 14.8898],
         [4.056, 25.6134],
         [4.9931, 38.3952],
         [5.8574, 43.5065],
         [7.1474, 91.3715],
         [8.1859, 119.075],
         [9.0349, 115.7737]]
    # Display results
    status, obj_val, sol_val = solve_curve_fitting(D, degree=2, objective=0)
    print("Status =", status)
    print("Objective value (min of sum (u + v)) =", obj_val)
    print("Solution a[] =", sol_val)
    # Draw the plot of the data points and the polynomial curve
    x = np.array(D)[:, 0]
    y = np.array(D)[:, 1]
    plt.scatter(x, y, marker='x', color='red')
    # Sum fit method
    a = sol_val
    x = np.linspace(min(x), max(x), 100)
    y = sum([a[i] * x ** i for i in range(len(a))])
    plt.plot(x, y, color='green')
    plt.legend(["Data", "Sum fit"])
    plt.show()


main()
