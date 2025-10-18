# Gas Blending problem
# This is a problem of preparing/mixing gasoline/oil, from crude oil
# refined finished product.
# The table consists of Gas, Octane, Min Demand, Max Demand, Price
from ortools.linear_solver import pywraplp


# C, D: The table of information about raw and refined products
def solve_gas(c, d):
    s = pywraplp.Solver('Gas Blending Problem',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    nR, nF = len(c), len(d)  # Number of raw and refined products
    Roc, Rmax, Rcost = 0, 1, 2  # Position of columns in table C
    Foc, Fmin, Fmax, Fprice = 0, 1, 2, 3  # Position of columns in table D
    # Decision variables of table G (2D Array)
    G = [[s.NumVar(0.0, 10000, '') for _ in range(nF)] for _ in range(nR)]
    # Decision variables of table R and table F
    R = [s.NumVar(0, c[i][Rmax], '') for i in range(nR)]
    F = [s.NumVar(d[j][Fmin], d[j][Fmax], '') for j in range(nF)]
    # Equations of the total of raw products and the total of refined products
    for i in range(nR):
        s.Add(R[i] == sum(G[i][j] for j in range(nF)))
    for j in range(nF):
        s.Add(F[j] == sum(G[i][j] for i in range(nR)))
    for j in range(nF):
        s.Add(F[j] * d[j][Foc] == s.Sum([G[i][j] * c[i][Roc] for i in range(nR)]))

    cost = s.Sum(R[i] * c[i][Rcost] for i in range(nR))
    price = s.Sum(F[j] * d[j][Fprice] for j in range(nF))
    s.Maximize(price - cost)
    status = s.Solve()
    # Extracting objective value (profit)
    obj_val = s.Objective().Value()
    # Extracting solution values for G (decision variables)
    sol_val = [[G[i][j].solution_value() for j in range(nF)] for i in range(nR)]
    return status, obj_val, sol_val


def main():
    # The table of raw gasoline products (C)
    C = [[99, 782, 55.34],
         [94, 894, 54.12],
         [84, 631, 53.68],
         [92, 648, 57.03],
         [87, 956, 54.81],
         [97, 647, 56.25],
         [81, 689, 57.55],
         [96, 609, 58.21]]
    # The table of refined gasoline products (D)
    D = [[88, 415, 11707, 61.97],
         [92, 479, 12596, 61.99],
         [94, 199, 7761, 62.04],
         [90, 479, 12596, 61.99]]
    status, value, G = solve_gas(C, D)
    print("Value of objective function (profit): {:0.2f}".format(value))
    for i in range(len(G)):
        for j in range(len(G[i])):
            print("{0:.1f} \t".format(G[i][j]), end=' ')
        print()


main()
