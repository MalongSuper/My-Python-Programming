# Maximize subject to the following constraints
# 0 ≤ x ≤ 1; 0 ≤ y ≤ 2; x + y ≤ 2
from ortools.linear_solver import pywraplp


def solve_model():
    # Create linear solver with Google Linear Optimization
    # solver = pywraplp.Solver.CreateSolver('GLOP')
    solver = pywraplp.Solver("Simple Linear Programming Example",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables
    x = solver.NumVar(0, 1, "x")  # x in [0, 1]
    y = solver.NumVar(0, 2, "y")  # y in [0, 2]
    # Constraints
    solver.Add(x + y <= 2)  # x + y ≤ 2
    # Objective Function
    obj_func = 3 * x + y
    solver.Maximize(obj_func)
    # Solve the problem
    status = solver.Solve()
    return (status, solver.Objective().Value(),
            x.solution_value(), y.solution_value())


def main():
    status, obj_val, x_val, y_val = solve_model()
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", obj_val)
        print("x =", x_val)
        print("y =", y_val)


main()
