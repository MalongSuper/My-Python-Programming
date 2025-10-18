# Shortest Path Tree with Linear Network Models Optimization
import numpy as np
from ortools.linear_solver import pywraplp


# D: distance matrix
def solve_shortest_path_tree(D, start=None):
    solver = pywraplp.Solver('Shortest Path Tree Problem',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(D)
    start = 0 if start is None else start

    # Decision Variables
    # G[i][j]: the number of shortest paths from node i to any intermediate node to node j
    # (including node j). For example, G[2][5] = 3 -> There are 3 shortest paths from node 2
    # to the nodes [5, 6, 11] through the intermediate node 5
    G = [[solver.NumVar(0, 0 if D[i][j] is None else n, '')
          for j in range(n)] for i in range(n)]

    # Constraints
    for i in range(n):
        if i == start:
            # start node/source: supply node, n - 1 output flow
            # No input floe
            solver.Add(sum(G[start][j] for j in range(n)) == n - 1)
            solver.Add(sum(G[j][start] for j in range(n)) == 0)  # Like supply noe
        else:
            # The number of shortest paths in node i - out of node i is equal to 1
            # Since node i is skipped
            solver.Add(sum(G[j][i] for j in range(n)) -
                       sum(G[i][j] for j in range(n)) == 1)

    # Objective Function
    # Minimize the total distances of all shortest paths
    solver.Minimize(solver.Sum(G[i][j] * (0 if D[i][j] is None else D[i][j])
                               for i in range(n) for j in range(n)))

    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[G[i][j].solution_value() for j in range(n)] for i in range(n)]
    SP_tree = [[i, j, D[i][j]] for i in range(n) for j in range(n)
               if G[i][j].solution_value() > 0]

    return status, obj_val, sol_val, SP_tree


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

    status, obj, G, SP_Tree = solve_shortest_path_tree(distance)
    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal objective value =', obj)
        print('Shortest Paths Tree')
        for node in SP_Tree:
            print(node)

        print("Decision Variables")
        for i in range(len(G)):
            for j in range(len(G[i])):
                if G[i][j] > 0:
                    print(f"G[{i}][{j}] = {G[i][j]}")
    else:
        print("The problems does not have an optimal solution")


main()
