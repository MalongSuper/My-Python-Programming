# This program solves Amphibian Coexistence
# x0: number of Toads
# x1: number of Salamanders
# x2: number of Caecilians
# Each of these species consume Worms, Crickets, Flies.
from ortools.linear_solver import pywraplp


def solve_coexistence(c):
    title_name = 'Amphibian Coexistence'
    # Create solver
    solver = pywraplp.Solver(title_name, pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables
    # x: 1D Array containing three decision variables x0, x1, x2 in range 1000
    # Maximum number of species is 1000
    x = [solver.NumVar(0, 1000, 'x[%i]' % i) for i in range(3)]
    # Constraints
    # Can be rewritten as mathematical formulas with various methods
    # e.g. a - b >= 0 or a >= b
    solver.Add(c[0][0] * x[0] + c[0][1] * x[1] + c[0][2] * x[2] <= c[0][3])
    solver.Add(c[1][0] * x[0] + c[1][1] * x[1] + c[1][2] * x[2] <= c[1][3])
    solver.Add(c[2][0] * x[0] + c[2][1] * x[1] + c[2][2] * x[2] <= c[2][3])
    # Objective function (Maximum of species)
    solver.Maximize(x[0] + x[1] + x[2])
    # Solve the problem
    solver.Solve()
    # Return the optimized value of the objective function
    return [round(entry.SolutionValue()) for entry in x]


def main():
    a11, a12, a13 = eval(input("Enter number of worms each species consumed "
                               "(In order: Toad, Salamander, Caecilian):\n"))
    b1 = int(input("Enter the number of available worms: "))
    a21, a22, a23 = eval(input("Enter number of crickets each species consumed "
                               "(In order: Toad, Salamander, Caecilian):\n"))
    b2 = int(input("Enter the number of available crickets: "))
    a31, a32, a33 = eval(input("Enter number of flies each species consumed "
                               "(In order: Toad, Salamander, Caecilian):\n"))
    b3 = int(input("Enter the number of available flies: "))
    c = [[a11, a12, a13, b1], [a21, a22, a23, b2], [a31, a32, a33, b3]]
    x = solve_coexistence(c)
    print(x)


main()
