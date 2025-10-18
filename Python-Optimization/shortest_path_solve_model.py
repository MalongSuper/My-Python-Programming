# The problem of finding the shortest path in the graph
# Using Network flow
from ortools.linear_solver import pywraplp


# d: Distance matrix
def solve_shortest_path(d, start=None, end=None):
    solver = pywraplp.Solver("Shortest Path Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(d)
    if start is None:
        start = 0
    if end is None:
        end = n - 1
    # Decision variables
    # X[i][j] in [0, 1] if there is a vertex from i to j
    # Conversely X[i][j] in [0, 0] means = 0
    X = [[solver.NumVar(0, 0 if d[i][j] is None else 1, '')
          for j in range(n)] for i in range(n)]
    # Constraints
    for i in range(n):
        # If "i" is the starting point (like source) there can exist many following paths
        # But there is only one path which is the shortest (sum = 1)
        # And source has no entry path (sum = 0)
        if i == start:
            solver.Add(sum(X[start][j] for j in range(n)) == 1)
            solver.Add(sum(X[j][start] for j in range(n)) == 0)
        # sink: One entry path and no following path
        elif i == end:
            solver.Add(sum(X[j][end] for j in range(n)) == 1)
            solver.Add(sum(X[end][j] for j in range(n)) == 0)
        else:  # Intermediate point based on the conservation of flow
            solver.Add(sum(X[i][j] for j in range(n)) == sum(X[j][i] for j in range(n)))
    # Objective function
    solver.Minimize(solver.Sum(X[i][j] * (0 if d[i][j] is None else d[i][j])
                               for i in range(n) for j in range(n)))
    status = solver.Solve()
    # Obtain solutions
    path, cost, cumulative_cost, node = [start], [0], [0], start
    while status == 0 and node != end and len(path) < n:
        next_node = [i for i in range(n) if X[node][i].solution_value() == 1][0]
        path.append(next_node)
        cost.append(d[node][next_node])
        cumulative_cost.append(cumulative_cost[-1] + cost[-1])
        node = next_node
    obj_val = solver.Objective().Value()
    sol_val = [[X[i][j].solution_value() for j in range(n)] for i in range(n)]
    return status, obj_val, sol_val, path, cost, cumulative_cost


def main():
    distance = [[None, 46, 17, 24, 51, None, None, None, None, None, None, None, None],
                [46, None, None, None, 31, 33, None, 54, None, None, None, None, None],
                [None, 38, None, None, 34, 31, None, None, 51, None, None, None, None],
                [24, None, None, None, 33, None, None, 17, 49, 31, None, None, None],
                [51, None, None, None, None, 4, None, None, 18, 39, 60, None, None],
                [48, None, None, None, 4, None, 4, None, 27, None, 35, 57, 51, None],
                [None, None, None, 33, 1, None, None, None, None, None, 59, None, None],
                [None, 54, 26, None, 32, 27, 31, None, None, 14, 42, 66, None],
                [None, None, 51, 49, 18, 20, 17, 43, None, None, 57, 32, None],
                [None, None, None, None, 39, 35, None, 14, None, None, 28, None, None],
                [None, None, None, None, 60, None, None, None, None, None, None, 58, 6],
                [None, None, None, None, None, None, None, None, 32, 61, 58, None, 56],
                [None, None, None, None, None, None, None, None, 59, None, None, 56, None]]
    status, obj_val, X, path, cost, cumulative_cost = solve_shortest_path(distance)
    if status == 0:
        print("Path:", path)
        print("Cost:", cost)
        print("Cumulative cost:", cumulative_cost)
        print("Objective value:", obj_val)
        print("Decision variables (X):")
        for i in range(len(X)):
            print(X[i])
    else:
        print("No solution")


main()
