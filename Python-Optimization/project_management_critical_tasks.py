# Project Management Problem with Critical Tasks
# Critical task is work that if started late
# will affect the entire project completion time
# This problem is solved using Network Flow (applying Shortest Path Solve Model)
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


# d: is the task description table
# t[i]: the time to start a task "i"
def critical_tasks(d, t):
    # s: the set of starting and ending points of all tasks
    # Since s is a set then there is no duplicates, in ascending order
    start_times = [t[i] for i in range(len(t))]
    end_times = [t[i] + d[i][1] for i in range(len(t))]
    s = set(start_times + end_times)
    s = sorted(s)  # Sort in ascending order
    n = len(s)
    start = min(s)
    end = max(s)
    # times: dictionary consisting ot key: the time to start the task
    # value: the order/label of the task in the plot
    times = {}
    idx = 0  # Index of the node in the plot
    for e in s:
        times[e] = idx
        idx += 1
    # Create a matrix of distance between two nodes (start and end times of the task)
    M = [[None for _ in range(n)] for _ in range(n)]
    for i in range(len(t)):
        # Because of finding the longest path, changed to -d[i][1]
        M[times[t[i]]][times[t[i] + d[i][1]]] = -d[i][1]
    # Obtain solutions
    status, obj_val, X, path, cost, cumulative_cost = solve_shortest_path(M, times[start], times[end])
    print("Objective value:", obj_val)
    print("Path", path)
    T = [i for i in range(len(t)) for time in path if times[t[i] + d[i][1]] == time]
    return status, T


def main():
    # D[i] = [task i, duration, {preceding tasks of task i}
    D = [[0, 7, {}],
         [1, 9, {}],
         [2, 12, {0}],
         [3, 8, {0, 1}],
         [4, 9, {3}],
         [5, 6, {2, 4}],
         [6, 5, {4}]]
    t = [0, 0, 7, 9, 17, 26, 26]
    status, T = critical_tasks(D, t)
    if status != 0:
        print("Infeasible")
    else:
        print("Critical tasks (T):", T)


main()
