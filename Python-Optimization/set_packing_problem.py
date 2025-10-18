# Set Packing problem
from ortools.linear_solver import pywraplp


# D: 2D Array consists of the Roster Numbers and the set of Crew Member ID
# C: The array of "Cost" of suppliers
def solve_set_cover(d, c=None):
    # Use either CBC_MIXED_INTEGER_PROGRAMMING or
    # SCIP_MIXED_INTEGER_PROGRAMMING
    solver = pywraplp.Solver('Airline Crew Scheduling (Set Packing Problem)',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    n_rosters = len(d)
    # Since Crew Member is ordered from 0, 1, 2 to n
    # The number of Crew Member is the largest number in array D incremented to 1
    n_crews = max(max(row) for row in d) + 1
    # Decision variables
    S = [solver.IntVar(0, 1, 'S[%d]' % i) for i in range(n_rosters)]
    # Constraints
    # Filter all the Roster Number that contains Crew Member ID j
    # And select no more than 1 Roster Number
    for j in range(n_crews):
        solver.Add(sum(S[i] for i in range(n_rosters) if j in d[i]) <= 1)
    # Objective function
    if c is None:
        solver.Maximize(solver.Sum(S))
    else:
        solver.Maximize(solver.Sum([S[i] * c[i] for i in range(n_rosters)]))
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    Rosters = [i for i in range(n_rosters) if S[i].solution_value() > 0]
    return status, obj_val, Rosters


def main():
    # D: 2D Array containing the Roster Number and the set of Crew Member IDs
    # Row i is the Roster Number i
    D = [[1, 18, 30],
         [4, 24, 36],
         [1, 5, 9],
         [7, 17, 30],
         [10, 23, 25],
         [8, 10, 25],
         [19, 29, 36],
         [3, 4, 17],
         [19, 28, 40],
         [11, 24, 31],
         [1, 30, 33],
         [22, 25, 26],
         [13, 15, 26],
         [21, 27, 28],
         [7, 12, 33]]
    status, obj_val, rosters = solve_set_cover(D)
    print("Status:", status)
    print("Objective value:", obj_val)
    print("Rosters:", rosters)


main()
