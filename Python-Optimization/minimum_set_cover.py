# Minimum Set Cover problem
from ortools.linear_solver import pywraplp


# D: 2D Array consists of the "part number" of each supplier
# C: The array of "Cost" of suppliers
def solve_set_cover(d, c=None):
    solver = pywraplp.Solver('Minimum Set Cover',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    n_suppliers = len(d)
    # Since "part number" is ordered from 0, 1, 2 to n
    # The number of "part number" is the largest number in array D incremented to 1
    n_parts = max(max(row) for row in d) + 1
    # Decision variables
    S = [solver.IntVar(0, 1, 'S[%d]' % i) for i in range(n_suppliers)]
    # Constraints
    # Filter all the suppliers that supply part j and find at least 1 supplier
    for j in range(n_parts):
        solver.Add(sum(S[i] for i in range(n_suppliers) if j in d[i]) >= 1)
    # Objective function
    if c is None:
        solver.Minimize(solver.Sum(S))
    else:
        solver.Minimize(solver.Sum([S[i] * c[i] for i in range(n_suppliers)]))

    status = solver.Solve()
    suppliers = [i for i in range(n_suppliers) if S[i].solution_value() > 0]
    parts = [[i for i in range(n_suppliers)
              if j in d[i] and S[i].solution_value() > 0] for j in range(n_parts)]
    obj_val = solver.Objective().Value()
    return status, obj_val, suppliers, parts


def main():
    D = [[3, 4, 5, 8, 24],
         [11, 15, 21, 23],
         [9, 15, 24],
         [9, 13],
         [5, 11, 12, 14, 16, 20],
         [8, 11, 12, 15, 21],
         [1, 4, 18, 20],
         [0, 3, 6, 11, 13, 15, 21, 23],
         [14, 16, 18, 19, 23],
         [2, 7, 16, 22],
         [10, 14, 21],
         [6, 19],
         [4, 10, 24],
         [3, 4, 7, 9, 17],
         [1, 3, 5, 6, 15, 18, 19, 20, 23]]
    status, obj_val, suppliers, parts = solve_set_cover(D)
    print("Status:", status)
    print("Objective value:", obj_val)
    print("Suppliers:", suppliers)
    print("Parts:")
    for i in parts:
        print(i)


main()
