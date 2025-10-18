# Maximum Flow Problem
from ortools.linear_solver import pywraplp


# Capacity matrix (C), Sources (S), Target/Sinks (T)
def solve_maxflow(c, s, t, unique=True):
    solver = pywraplp.Solver("Maximum Flow Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    n = len(c)
    # Decision variables
    # X[i][j]: flow starts from node i to node j
    X = [[solver.NumVar(0, c[i][j], f'x_{i}_{j}')
          for j in range(n)] for i in range(n)]
    # B: The sum of all the capacities can be transported in the network
    B = sum(c[i][j] for i in range(n) for j in range(n))
    # Upper bound does not exceed B
    flow_out = solver.NumVar(0, B, 'flow_out')
    flow_in = solver.NumVar(0, B, 'flow_in')
    # Constraints
    for i in range(n):
        if (i not in s) and (i not in t):  # Intermediate node i
            # With the intermediate nodes, the external flow must be equal to the internal flow
            solver.Add(sum(X[i][j] for j in range(n)) == sum(X[j][i] for j in range(n)))
    solver.Add(flow_out == sum(X[i][j] for i in s for j in range(n)))
    solver.Add(flow_in == sum(X[j][i] for i in s for j in range(n)))
    # Objective functions
    # net_flow: there can be many optimal solutions, but the optimal value remains unchanged
    # So, we only need to find one of them
    net_flow = (flow_out - flow_in)
    # dual_objective: ensure that the optimal solution is consistent
    dual_objective = (flow_out - 2 * flow_in)
    solver.Maximize(dual_objective if unique else net_flow)
    status = solver.Solve()
    sol_val_ft = flow_out.solution_value()
    sol_val_fn = flow_in.solution_value()
    sol_val_x = [[X[i][j].solution_value() for j in range(n)] for i in range(n)]
    return status, sol_val_ft, sol_val_fn, sol_val_x


def main():
    # Source node 0 to source node 3 of the following capacity matrix
    capacity = [[0, 4, 0, 0],
                [0, 0, 0, 5],
                [0, 3, 0, 0],
                [0, 0, 0, 0]]
    # Sources and targets
    S = [0, 2]
    T = [3]
    status, flow_out, flow_in, X = solve_maxflow(capacity, S, T, unique=True)
    print("Value of objective function")
    print("Flow out: {:0.2f}".format(flow_out))
    print("Flow in: {:0.2f}".format(flow_in))
    print("Optimal solution:")
    for i in range(len(X)):
        for j in range(len(X[i])):
            print("{:2.0f}".format(X[i][j]), end=" ")
        print()

    print()
    # Source node 0 to source node 4 of the following capacity matrix
    capacity = [[0, 20, 30, 10, 0],
                [0, 0, 40, 0, 30],
                [0, 0, 0, 10, 20],
                [0, 0, 5, 0, 20],
                [0, 0, 0, 0, 0]]
    # Sources and targets
    S = [0, 2]
    T = [4]
    status, flow_out, flow_in, X = solve_maxflow(capacity, S, T, unique=True)
    print("Value of objective function")
    print("Flow out: {:0.2f}".format(flow_out))
    print("Flow in: {:0.2f}".format(flow_in))
    print("Optimal solution:")
    for i in range(len(X)):
        for j in range(len(X[i])):
            print("{:2.0f}".format(X[i][j]), end=" ")
        print()

    print()
    # Source node 0 to source node 6 of the following capacity matrix
    capacity = [[0, 0, 0, 21, 0, 0, 0],
                [0, 0, 29, 0, 28, 0, 23],
                [0, 0, 0, 24, 10, 0, 16],
                [23, 25, 19, 0, 28, 0, 0],
                [0, 0, 17, 15, 0, 29, 19],
                [30, 0, 0, 16, 30, 0, 0],
                [0, 20, 22, 0, 30, 0, 0]]
    # Sources and targets
    S = [0, 2]
    T = [6]
    status, flow_out, flow_in, X = solve_maxflow(capacity, S, T, unique=True)
    print("Value of objective function")
    print("Flow out: {:0.2f}".format(flow_out))
    print("Flow in: {:0.2f}".format(flow_in))
    print("Optimal solution:")
    for i in range(len(X)):
        for j in range(len(X[i])):
            print("{:2.0f}".format(X[i][j]), end=" ")
        print()
    print()


main()
