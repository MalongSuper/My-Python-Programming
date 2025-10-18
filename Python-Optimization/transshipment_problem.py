# Network Flow Problem - Transshipment Problem
from ortools.linear_solver import pywraplp


# D: cost matrix, the row is the demand, the last column is the supply
def solve_transshipment(d):
    solver = pywraplp.Solver("Transshipment Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(d) - 1
    B = sum(d[-1][j] for j in range(n))  # Total of demand
    # Decision Variables
    G = [[solver.NumVar(0, B if d[i][j] else 0, f'G_{i}_{j}')
          for j in range(n)] for i in range(n)]
    # Constraints
    # For every node: (Flow out - Flow in) = (supply - demand)
    for i in range(n):
        solver.Add(sum(G[i][j] for j in range(n)) - sum(G[j][i] for j in range(n))
                   == d[i][-1] - d[-1][i])
    # Objective Function
    Cost = solver.Sum(G[i][j] * d[i][j] for i in range(n) for j in range(n))
    solver.Minimize(Cost)
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[G[i][j].solution_value() for j in range(n)] for i in range(n)]
    return status, obj_val, sol_val


def main():
    # Cost Matrix
    D = [[0, 0, 0, 0, 17, 10, 19, 0, 0],
         [23, 0, 0, 28, 0, 23, 0, 0, 0],
         [29, 0, 0, 0, 30, 25, 25, 0, 680],
         [0, 0, 0, 0, 17, 15, 19, 29, 0],
         [0, 16, 0, 0, 0, 0, 0, 0],
         [22, 0, 0, 0, 25, 0, 0, 18, 540],
         [25, 29, 16, 0, 0, 22, 0, 0, 0],
         [0, 0, 30, 0, 10, 0, 27, 0, 0],
         [241, 0, 0, 164, 239, 0, 152, 424, 0]]

    status, min_cost, G = solve_transshipment(D)
    print("Minimum Cost:", min_cost)
    for i in range(len(G)):
        print(G[i])


main()
