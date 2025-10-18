# Non-Linear Function Minimization
# Finding minimize of a non-linear function via Linear Approximations
# The non-linear function is approximated by the piecewise linear functions
# Solve minimize of f(x) = sin(x) * e^x in range [2, 8]
from ortools.linear_solver import pywraplp


# Points: 2D Array including value Bi in the respective Total Cost
# B: bound
def minimize_piecewise_linear_convex(points, b):
    s = pywraplp.Solver('Piecewise Linear',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(points)
    x = s.NumVar(points[0][0], points[n - 1][0], 'x')
    # d: Decision variable delta (δ)
    d = [s.NumVar(0.0, 1, 'd[%i]' % (i, )) for i in range(n)]
    # Constraints
    s.Add(1 == sum(d[i] for i in range(n)))
    s.Add(x == sum(d[i] * points[i][0] for i in range(n)))
    s.Add(x >= b)
    # Solution
    cost = s.Sum(d[i] * points[i][1] for i in range(n))
    s.Minimize(cost)
    s.Solve()
    # Return the value of the decision variable delta
    R = [d[i].SolutionValue() for i in range(n)]
    return R


# Func: non-linear function that needs to find minimize
def minimize_non_linear(func, left, right, precision):
    n = 5  # 5 points in the function plot --> 4 linear points
    x = 0.0
    while right - left > precision:
        dta = (right - left) / (n - 1.0)  # delta: distance between points
        # points: list of points in the function plot
        points = [(left + dta * i, func(left + dta * i)) for i in range(n)]
        # G: the value of the delta (δ)
        G = minimize_piecewise_linear_convex(points, left)
        # x: value x at the minimize point
        x = sum([G[i] * points[i][0] for i in range(n)])
        # left, right: the new limit of the point that needs to find minimize
        # G[i] > 0: The point i, which is the last point of the linear points
        # index of each point has G[i] > 0
        indices = [i - 1 for i in range(n) if G[i] > 0]
        left = points[max(0, indices[0])][0]
        # Simplify: left = points[max(0, [i - 1 for i in range(n) if G[i] > 0][0])][0]
        right = points[min(n - 1, [i + 1 for i in range(n - 1, 0, -1) if G[i] > 0][0])][0]
    return x


def main():
    # Finding minimize of f(x) = sin(x) * e^x in range [2, 8]
    # Precision = 0.05
    def func(x):
        from math import sin, exp
        return sin(x) * exp(x)

    left = 2
    right = 8
    precision = 0.05
    x = minimize_non_linear(func, left, right, precision)
    print("Min at x: {:0.1f}".format(x))
    print("Min value: {:0.1f}".format(func(x)))


main()
