# Power Supply Model (Minimum Cost Flow Problem)
from ortools.linear_solver import pywraplp


# d: 2D array (matrix) of the cost
def solve_min_cost(d):
    solver = pywraplp.Solver("Minimum Cost Flow Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    m = len(d) - 1  # Number of plants, exclude the demand row
    n = len(d[0]) - 1  # Number of cities, exclude the supply column
    B = sum(d[-1][j] for j in range(n))  # Total of peak demand
    # Decision variables
    # X[i][j]: the real flow starts from plant i to plant j
    X = [[solver.NumVar(0, B if d[i][j] else 0, f'X_{i}_{j}')
          for j in range(n)] for i in range(m)]
    # Constraints
    # The total of supply of each plant must not exceed the capacity
    for i in range(m):
        solver.Add(sum(X[i][j] for j in range(n)) <= d[i][-1])
    # The total of demand of each city at peak
    for j in range(n):
        solver.Add(sum(X[i][j] for i in range(m)) == d[-1][j])
    # Total cost
    cost = solver.Sum(X[i][j] * d[i][j] for i in range(m) for j in range(n))
    solver.Minimize(cost)
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[X[i][j].solution_value() for j in range(n)] for i in range(m)]
    return status, obj_val, sol_val


def main():
    # Cost matrix
    D = [[23, 0, 19, 25, 14, 0, 281, 551],
         [16, 0, 0, 20, 23, 13, 0, 689],
         [22, 18, 11, 0, 20, 13, 0, 634],
         [288, 234, 236, 231, 247, 262, 281, 0]]
    status, min_cost, X = solve_min_cost(D)
    print("Minimum cost: {:0.2f}".format(min_cost))
    for i in range(len(X)):
        print(X[i])


main()
