# Traveling salesman problem (sub-tour elimination constraint)
# Directed graph
from ortools.linear_solver import pywraplp


# D: distances matrix; sub-tour[[]]: 2D-list, set of sub-tours
def solve_tsp_eliminate(d, sub_tours=None):
    if sub_tours is None:
        sub_tours = []
    solver = pywraplp.Solver('TSP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    n = len(d)
    # Decision variables
    x = [[solver.IntVar(0, 0 if d[i][j] == 0 else 1, "x[%d,%d]" % (i, j))
          for j in range(n)] for i in range(n)]
    # Constraints
    for i in range(n):
        solver.Add(solver.Sum(x[i][j] for j in range(n)) == 1)
        solver.Add(solver.Sum(x[j][i] for j in range(n)) == 1)
        solver.Add(x[i][i] == 0)
    # Sub-tour elimination constraints
    # An arbitrary sub-tour => The total of arcs is equal to the vertex
    # Exclude forming sub-tour by constraining the total of arcs
    for sub in sub_tours:
        solver.Add(solver.Sum(x[i][j] for i in sub for j in sub) <= len(sub) - 1)
    # Objective function
    solver.Minimize(solver.Sum(x[i][j] * (0 if d[i][j] is None else d[i][j])
                               for i in range(n) for j in range(n)))
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[x[i][j].solution_value() for j in range(n)] for i in range(n)]
    # Convert to the matrix of decision variable x to a matrix of entry X
    X = sol_val
    tours = extract_tours(X, n)
    return status, obj_val, tours


def extract_tours(x, n):
    node = 0
    tours = [[0]]
    all_nodes = [0] + [1] * (n - 1)
    # Iterate until the remaining number of vertices = 0
    # Meaning the tours that the solver returns is 1
    while sum(all_nodes) > 0:
        next_node = [i for i in range(n) if x[node][i] == 1][0]
        if next_node not in tours[-1]:
            tours[-1].append(next_node)
            node = next_node
        else:
            node = all_nodes.index(1)
            tours.append([node])
        all_nodes[node] = 0
    return tours


def solve_tsp(D):
    sub_tours = []
    tours = []
    status, obj_val = 0, 0
    # When tours is only 1 tour then stops the iteration (the biggest tour)
    while len(tours) != 1:
        status, obj_val, tours = solve_tsp_eliminate(D, sub_tours)
        if status == 0:
            sub_tours.extend(tours)  # Add all tours to sub tours
            print("Set of sub tours:", tours)
    return status, obj_val, tours[0]


def main():
    D = [
        [0, 711, 107, 516, 387, 408, 539, 309, 566, 771],
        [539, 0, 769, 881, 380, 546, 655, 443, 295, 1140],
        [122, 752, 0, 281, 441, 264, 318, 448, 588, 730],
        [519, 875, 274, 0, 435, 334, 93, 776, 949, 302],
        [484, 561, 338, 419, 0, 118, 268, 607, 495, 431],
        [409, 406, 244, 380, 93, 0, 295, 544, 549, 494],
        [479, 735, 334, 101, 345, 247, 0, 679, 809, 238],
        [221, 444, 433, 744, 487, 435, 649, 0, 325, 840],
        [510, 303, 599, 984, 531, 553, 847, 350, 0, 1001],
        [663, 989, 664, 335, 588, 434, 297, 1093, 1012, 0]
    ]

    status, obj_val, tour = solve_tsp(D)
    print("Status:", status)
    print("Total distances:", obj_val, "miles")
    print("Route:", tour)


main()
