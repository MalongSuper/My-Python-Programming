# Bin Packing Problem
from ortools.linear_solver import pywraplp


def solve_bin_packing(d, w):
    solver = pywraplp.Solver('Bin Packing Problem',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # n_items = len(d)
    n_packages = sum([item[0] for item in d])  # sum(D[i]) for i in range(n_items)
    n_trucks = n_packages  # Maximum number of trucks
    # For example, transfer 8 packages with the maximum weight 258kg/package
    # to a sequence of 8 value 258
    weights = []
    for item in d:
        weights += item[0] * [item[1]]
    # Decision variables
    # x[i][j] = 1 if the package i is placed at truck j
    x = [[solver.IntVar(0, 1, f'x[{i}][{j}]')
          for j in range(n_trucks)] for i in range(n_packages)]
    # y[k] = 1 if the truck k is used
    y = [solver.IntVar(0, 1, '') for _ in range(n_trucks)]
    # Constraints
    # Each package is only placed in one truck
    for i in range(n_packages):
        # Use this or solver.Add(sum(x[i]) == 1
        solver.Add(sum(x[i][j] for j in range(n_trucks)) == 1)
    # The weight of the packages in one truck does not exceed the capacity
    for j in range(n_trucks):
        solver.Add(sum(weights[i] * x[i][j] for i in range(n_packages)) <= w * y[j])
    # Objective function
    min_n_trucks = sum([y[j] for j in range(n_trucks)])
    solver.Minimize(min_n_trucks)
    # Solve the problem
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [y[i].solution_value() for i in range(n_trucks)]
    return status, obj_val, sol_val


def main():
    # D: The quantity and weight of the packages
    D = [[8, 258], [10, 478], [1, 399]]
    # W: Maximum Capacity (load) of a truck
    W = 1264
    status, obj_val, y = solve_bin_packing(D, W)
    print("Status =", status)
    print("Objective Value =", obj_val)
    print("Solution Value =", y)


main()
