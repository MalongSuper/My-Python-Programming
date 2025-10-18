# Bin Packing Problem
from ortools.linear_solver import pywraplp


def solve_bin_packing(d, w, symmetry_breaking=False):
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

    # Symmetry breaking (add this to the solve_bin_packing() function)
    if symmetry_breaking:
        # the trucks can be selected in order
        for k in range(n_trucks - 1):
            solver.Add(y[k] >= y[k + 1])

        # Analyze each group of packages with the same weight
        # If a package j is put on the truck k, then the packages are in the same group as i
        # But before j need to put on the truck k or on one of the trucks after k
        index = 0
        n_groups = len(d)
        for i in range(n_groups):
            lj = index  # lower bound
            uj = index + d[i][0]  # upper bound
            for j in range(lj, uj):
                for k in range(n_trucks):
                    # the packages are in the same group as j
                    # but precedes j must be put on truck k or before k
                    for jj in range(max(lj, j - 1), j):
                        solver.Add(sum(x[jj][kk] for kk in range(0, k + 1)) >= x[j][k])
                    # The packages with the same group as j
                    # but succeed j must be put  on truck k or after k
                    for jj in range(j + 1, min(j + 2, uj)):
                        solver.Add(sum(x[jj][kk] for kk in range(k, n_trucks)) >= x[j][k])
            index += d[i][0]

    # Objective function
    min_n_trucks = sum([y[j] for j in range(n_trucks)])
    solver.Minimize(min_n_trucks)
    # Solve the problem
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    # Extract solution
    sol_x = [[int(x[i][j].solution_value()) for j in range(n_trucks)] for i in range(n_packages)]
    sol_y = [int(y[j].solution_value()) for j in range(n_trucks)]
    return status, obj_val, sol_x, sol_y


def get_weights(d):
    weights = []
    for item in d:
        weights += item[0] * [item[1]]
    return weights


def main():
    # D: The quantity and weight of the packages
    D = [[8, 258], [10, 478], [8, 399]]
    # W: Maximum Capacity (load) of a truck
    W = 1264
    print("Processing...")

    status, obj_val, x, y = solve_bin_packing(D, W, symmetry_breaking=True)
    print("Status =", status)
    print("Objective Value =", obj_val)
    print("Solution Value =", y)

    # Display solution
    weights = get_weights(D)
    print("Weight:", weights)
    # The packages in each truck
    n = int(obj_val)
    for j in range(n):
        truck_items = [weights[i] for i in range(len(x))
                       if x[i][j] == 1 and y[j] == 1]
        print(f"Truck {j}: {truck_items}")


main()
