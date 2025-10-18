# Maximize subject to the following constraints
# x + 2y ≤ 14; 3x - y ≥ 0; x - y ≤ 2
# 0 ≤ x ≤ 4; 0 ≤ y ≤ 6
from ortools.linear_solver import pywraplp
import numpy as np
import matplotlib.pyplot as plt


def solve_model(obj_func):
    # Create linear solver with Google Linear Optimization
    # solver = pywraplp.Solver.CreateSolver('GLOP')
    solver = pywraplp.Solver("Simple Linear Programming Example",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables
    x = solver.NumVar(0, 4, "x")  # x in [0, 4]
    y = solver.NumVar(0, 6, "y")  # y in [0, 6]
    # Constraints
    solver.Add(x + 2 * y <= 14)  # x + 2y ≤ 14
    solver.Add(3 * x - y >= 0)  # 3x - y ≥ 0
    solver.Add(x - y <= 2)  # x - y ≤ 2
    # Create the objective function: f(x, y) = obj_func(x, y)
    objective = solver.Objective()
    # Assuming obj_func is a lambda function like: lambda x, y: 3*x + 4*y
    # We'll extract the coefficients for x and y
    objective.SetCoefficient(x, obj_func[0])  # Coefficient for x
    objective.SetCoefficient(y, obj_func[1])  # Coefficient for y
    objective.SetMaximization()  # Maximize the objective
    # Solve the problem
    status = solver.Solve()
    return (status, solver.Objective().Value(),
            x.solution_value(), y.solution_value())


def draw_plot(fxy):
    x_vals = np.linspace(0, 6, 500)
    y1 = (14 - x_vals) / 2  # x + 2y = 14
    y2 = 3 * x_vals  # 3x - y = 0
    y3 = x_vals - 2  # x - y ≤ 2
    # Draw plot
    plt.figure(figsize=(8, 6.5))
    # Plot constraint lines with labels
    plt.plot(x_vals, y1, color="black", label=r"$x + 2y = 14$")  # x + 2y = 14
    plt.plot(x_vals, y2, color="black", label=r"$3x - y = 0$")  # 3x - y = 0
    plt.plot(x_vals, y3, color="black", label=r"$x - y = 2$")  # x - y = 2
    # Add labels to lines
    plt.text(3, 5.2, "x + 2y = 14", fontsize=8, rotation=-20)
    plt.text(1, 4, "3x - y = 0", fontsize=8, rotation=65)
    plt.text(4, 0.5, "x - y = 2", fontsize=8, rotation=-45)
    # Set plot limits and labels
    plt.xlim(-2, 8)
    plt.ylim(-4, 6)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Maximize {fxy}")
    # Draw axes
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(alpha=0.3)
    plt.show()


def main():
    print("Find maximize in equation (Constraints Solve Model)")
    fxy = input("Enter exact equation f(x): ")
    # Extract coefficients for the objective function
    terms = fxy.split('+')
    obj_func = [int(term.split('*')[0]) if '*' in term
                else int(term) for term in terms]
    status, obj_val, x_val, y_val = solve_model(obj_func)
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", obj_val)
        print(x_val)
        print(y_val)
        draw_plot(fxy)


main()
