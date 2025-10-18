# This program finds the maximum integer
# Using optimization
from ortools.linear_solver import pywraplp
import numpy as np
# Idea: For a min encountered, set its index as 1, the others are 0


def solve_model(x, k):
    # Create linear solver with Solving Constraint Integer Program
    solver = pywraplp.Solver.CreateSolver("SCIP")
    n = len(x)
    # Decision variables
    # Using the idea, the number is either not min (0.0) or min (1.0)
    # X in {0, 1}
    y = [solver.IntVar(0, 1, f"y[{i}]") for i in range(n)]
    # Constraints
    # e.g. If we want to find 2 minimum values (k = 2)
    # then their marked index sum is 1.0 + 1.0 = 2.0, equal to k
    solver.Add(solver.Sum(y) == k)
    # Objective function
    solver.Minimize(solver.Sum(x[i] * y[i] for i in range(n)))
    # Solve the problem
    status = solver.Solve()
    return (status, solver.Objective().Value(),
            [y[i].solution_value() for i in range(n)])


def main():
    n = int(input("Enter size of the array: "))
    X = np.random.randint(1, 20, size=n)
    k = int(input("Enter the number of Min: "))
    print("Array:", X)
    status, obj_val, y = solve_model(X, k)
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", obj_val)
        print("y =", y)


main()
