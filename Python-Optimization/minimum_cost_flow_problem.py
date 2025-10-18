# Minimum Cost Flow Problem
# A table of workers, tasks and costs
# Minimize the total cost to complete the job
from ortools.linear_solver import pywraplp


def solve_min_cost(d):
    solver = pywraplp.Solver("Minimum Cost Flow Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    m = len(d)  # Number of workers
    n = len(d[0])  # Number of tasks
    # Decision variables
    # X[i][j] = 1 if worker i does job j
    X = []
    for i in range(m):
        X.append([solver.BoolVar(f"X_{i}_{j}") for j in range(n)])
    # Constraints
    # Each worker only does one task
    for i in range(m):
        solver.Add(sum(X[i][j] for j in range(n)) == 1)
    # Two workers cannot do the same task
    for j in range(n):
        solver.Add(sum(X[i][j] for i in range(n)) == 1)
    # When the number of task is greater than the number of workers
    # There exists a worker who does not do any task
    # Minimize the cost
    cost = solver.Sum(X[i][j] * d[i][j] for i in range(m) for j in range(n))
    solver.Minimize(cost)
    status = solver.Solve()
    obj_val = solver.Objective().Value()
    sol_val = [[X[i][j].solution_value() for j in range(n)] for i in range(m)]
    return status, obj_val, sol_val


def main():
    data = [[90, 80, 75, 70],
            [35, 85, 55, 65],
            [125, 95, 90, 95],
            [45, 110, 95, 115],
            [50, 100, 90, 100]]
    status, min_cost, X = solve_min_cost(data)
    print("Minimum cost: {:0.2f}".format(min_cost))
    for i in range(len(X)):
        print(X[i])
    # Display the optimal task assignment
    for i in range(len(X)):
        for j in range(len(X[0])):
            if X[i][j] > 0:
                print(f"Worker {i} assigned to task {j} with cost {data[i][j]}")


main()
