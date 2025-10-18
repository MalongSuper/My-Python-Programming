# Piecewise Linear: Executable model
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


def calculate_cost(points, b, unit_cost):
    for i in range(len(unit_cost), -1, -1):
        if points[i][0] < b:
            total_cost = (b - points[i][0]) * unit_cost[i]
            print(points[i][0], unit_cost[i])
            print(total_cost)


def main():
    print("Piecewise Linear")
    # [310, 8088] means when Bi = 310, Total Cost = 8088
    # Example: from 0 to 148, Total Cost = [0, 3552]
    # from 148 to 310, Total Cost = [3552, 8088]
    # from 310 to 501, Total Cost = [8088, 14200]
    # and so on
    points = [[0, 0], [148, 3552], [310, 8088], [501, 14200],
              [617, 18144], [762, 23364], [959, 31244]]
    unit_cost = [24, 28, 32, 34, 36, 40]
    B = int(input("Enter B: "))  # The piecewise B (x ≥ B)
    R = minimize_piecewise_linear_convex(points, B)
    # Display solutions
    print("δ =", R)
    print()
    # Display tables
    print("{:>5}{:>8}{:>10}{:>13}"
          .format("Interval", "δi", "xi", "f(xi)"))
    for i in range(len(R)):
        print("{:>0}\t\t\t{:.4f}\t\t{:<10}{:<10}".format(i, R[i], points[i][0], points[i][1]))
    print("Summation of δ =", sum(R))
    print("x =", B)
    # Calculate the cost
    calculate_cost(points, B, unit_cost)


main()
