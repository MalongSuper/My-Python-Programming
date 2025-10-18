# Resource Allocation Problem
from ortools.linear_solver import pywraplp


def solve_resource_allocation(num_resources, num_activities,
                              profits, available_resources, costs):
    solver = pywraplp.Solver.CreateSolver("GLOP")
    infinity = solver.Infinity()
    # Decision variables
    var_x = [solver.NumVar(0, infinity, name=f"x_P{a}")
             for a in range(num_activities)]
    # Objective function
    solver.Maximize(solver.Sum([profits[a] * var_x[a]
                                for a in range(num_activities)]))
    # Constraints
    for r_idx in range(num_resources):
        solver.Add(solver.Sum([costs[r_idx][a_idx] * var_x[a_idx]
                               for a_idx in range(num_activities)]) <= available_resources[r_idx])
    status = solver.Solve()
    if status != pywraplp.Solver.OPTIMAL:
        print("Solver failure!")
    print("Solve complete!")
    opt_obj = solver.Objective().Value()
    print(f"Optimal objectives = {opt_obj: .2f}")
    opt_sol = [var_x[a_idx].solution_value()
               for a_idx in range(num_activities)]
    for a_idx in range(num_activities):
        print(f"opt_x[{a_idx + 1}] = {opt_sol[a_idx]: .2f}")


def main():
    num_resources = 3
    num_activities = 5
    profits = [1223, 1238, 1517, 1616, 1027]
    available_resources = [2001, 2616, 1691]
    costs = [[90, 57, 51, 97, 67],
             [64, 58, 97, 56, 93],
             [55, 87, 77, 52, 51]]
    solve_resource_allocation(num_resources, num_activities,
                              profits, available_resources, costs)


main()
