# Workforce Planning Problem
from ortools.linear_solver import pywraplp


def solve_workforce_planning(num_periods, num_patterns, requirements, costs, patterns):
    solver = pywraplp.Solver.CreateSolver('GLOP')
    infinity = solver.Infinity()
    # Decision variables
    var_p = [solver.NumVar(0, infinity, name=f"x_{p}")
             for p in range(num_patterns)]
    # Objective function
    solver.Minimize(solver.Sum([costs[p] * var_p[p] for p in range(num_patterns)]))
    # Constraints
    for t in range(num_periods):
        solver.Add(solver.Sum([var_p[p] for p in range(num_patterns)
                               if (t + 1) in patterns[p]]) >= requirements[t])
    # Solve the problem and retrieve optimal solution
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Objective = {solver.Objective().Value()}")
        for p in range(num_patterns):
            print(f"var_{p + 1} = {var_p[p].solution_value()}")


def main():
    # import instance data
    num_periods = 10
    num_patterns = 4
    requirements = [3, 4, 3, 1, 5, 7, 2, 4, 5, 1]
    costs = [10, 30, 20, 40]
    patterns = [set([1, 2, 3, 4]),
                set([3, 4, 5]),
                set([4, 5, 6, 7]),
                set([7, 8, 9, 10])]
    solve_workforce_planning(num_periods, num_patterns, requirements, costs, patterns)


main()
