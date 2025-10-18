# Transportation Problem
from ortools.linear_solver import pywraplp


def solve_transportation(num_sources, num_destinations, supplies, demands, costs):
    # Create solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    # Decision variables
    var_flow = []
    for src_idx in range(num_sources):
        variables = [solver.NumVar(0, solver.Infinity(),
                                   name=f"var_{src_idx}, {dest_idx}") for dest_idx in range(num_destinations)]
        var_flow.append(variables)
    # Constraints
    for src_idx in range(num_sources):
        expr = [var_flow[src_idx][dest_idx]
                for dest_idx in range(num_destinations)]
        solver.Add(solver.Sum(expr) == supplies[src_idx])
    for dest_idx in range(num_destinations):
        expr = [var_flow[src_idx][dest_idx]
                for src_idx in range(num_sources)]
        solver.Add(solver.Sum(expr) == demands[dest_idx])
    # Objective functions
    obj_expr = []
    for src_idx in range(num_sources):
        for dest_idx in range(num_destinations):
            obj_expr.append(var_flow[src_idx][dest_idx] * costs[src_idx][dest_idx])
    solver.Minimize(solver.Sum(obj_expr))
    status = solver.Solve()
    opt_flow = []
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Optimal objective = {solver.Objective().Value()}")
        for src_idx in range(num_sources):
            opt_vals = [var_flow[src_idx][dest_idx].solution_value()
                        for dest_idx in range(num_destinations)]
            opt_flow.append(opt_vals)
    return opt_flow


def main():
    num_sources = 4
    num_destinations = 5
    supplies = [58, 55, 64, 71]
    demands = [44, 28, 36, 52, 88]
    costs = [[8, 5, 13, 12, 12],
             [8, 7, 18, 6, 5],
             [11, 12, 5, 11, 18],
             [19, 13, 5, 10, 18]]
    solve_transportation(num_sources, num_destinations, supplies, demands, costs)


main()
