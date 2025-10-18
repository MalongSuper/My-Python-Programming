# Solve Lady or Tigers Problem using Optimization
# A prisoner is faced with nine doors, one of which he must open.
# Behind one door awaits a lady; behind the others, a tiger, if anything
# Objective: The prisoner manages to find the door of the lady's
# Advanced Techniques with Reify force, Reify Raise, etc.
from ortools.linear_solver import pywraplp


def new_solver(name, integer=False):
    return pywraplp.Solver(name, pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING
        if integer else pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


def new_IntVar(s, lb, ub):
    L = ub - lb + 1
    x = [s.IntVar(lb, ub, "")] + [s.IntVar(0, 1, "") for _ in range(L)]
    s.Add(1 == sum(x[k] for k in range(1, L + 1)))
    s.Add(x[0] == sum((lb + k - 1) * x[k] for k in range(1, L + 1)))
    return x


# Use these functions to xtract Values from the OR-Tools objects - For Advanced problems
def sol_val(x):
    if type(x) is not list:
        return 0 if x is None \
            else x if isinstance(x, (int, float)) \
            else x.solution_value() if x.Integer is False \
            else int(x.solution_value())
    elif type(x) is list:
        return [sol_val(e) for e in x]


def obj_val(x):
    return x.Objective().Value()


def k_out_of_n(s, k, x, relation=""):
    n = len(x)
    binary = (sum(x[i].Lb() == 0 for i in range(n)) == n
              and sum(x[i].Ub() == 1 for i in range(n)) == n)
    if binary:
        L = x
    else:
        L = [s.IntVar(0, 1, "") for _ in range(n)]
        for i in range(n):
            if x[i].Ub() > 0:
                s.Add(x[i] <= x[i].Ub() * L[i])
            else:
                s.Add(x[i] >= x[i].Lb() * L[i])
    S = sum(L[i] for i in range(n))
    if relation == '==' or relation == '=':
        s.Add(S == k)
    elif relation == '>=':
        s.Add(S >= k)
    else:
        s.Add(S <= k)
    return L


def bounds_on_box(a, x, b):  # Compute bounds on linear functions
    bounds, n = [None, None], len(a)
    s = pywraplp.Solver('Bounds on Box Problem',
                        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables: Create a copy of the
    # provided parameter x instead of using the parameter itself
    xx = [s.NumVar(x[i].Lb(), x[i].Ub(), "") for i in range(n)]
    S = s.Sum([-b] + [a[i] * xx[i] for i in range(n)])
    # Objective function
    s.Maximize(S)
    status = s.Solve()
    bounds[1] = None if status != 0 else s.Objective().Value()
    s.Minimize(S)
    s.Solve()
    bounds[0] = None if status != 0 else s.Objective().Value()
    return bounds


# Reify a constraint to a zero-one variable δ
# and enforce the constraint whenever δ is set
def reify_force(s, a, x, b, delta=None,
                relation='<=', bounds=None):
    # delta == 1 --> a * x <= b
    n = len(a)
    if delta is None:
        delta = s.IntVar(0, 1, "")
    if bounds is None:
        # Use this function to find tight lower and upper bounds
        bounds = bounds_on_box(a, x, b)
    # Add the appropriately modified constraint, either an
    # implementation of equation for a “less than or equal to” relation or the
    # corresponding constraint for a "greater than or equal than".
    if relation in ['<=', '==']:
        s.Add(sum(a[i] * x[i] for i in range(n)) <= b + bounds[1] * (1 - delta))
    if relation in ['>=', '==']:
        s.Add(sum(a[i] * x[i] for i in range(n)) >= b + bounds[1] * (1 - delta))
    return delta


def reify_raise(s, a, x, b, delta=None, relation='<=', bounds=None, eps=1):
    # a * x <= b --> delta == 1
    n = len(a)
    if delta is None:
        delta = s.IntVar(0, 1, "")
    if bounds is None:
        bounds = bounds_on_box(a, x, b)
    if relation == '<=':
        s.Add(sum(a[i] * x[i] for i in range(n))
              >= b + bounds[0] * delta + eps * (1 - delta))
    if relation == '>=':
        s.Add(sum(a[i] * x[i] for i in range(n))
              <= b + bounds[0] * delta + eps * (1 - delta))
    elif relation == '==':
        # The left-hand side can be either greater
        # or smaller than the right-hand side.
        # This is why we introduce two other binary variables, gm[0] (really γ0)
        # and gm[1] (really γ1), to reflect each type of violation
        gm = [s.IntVar(0, 1, "") for _ in range(2)]
        s.Add(sum(a[i] * x[i] for i in range(n))
              >= b + bounds[0] * gm[0] + eps * (1 - gm[0]))
        s.Add(sum(a[i] * x[i] for i in range(n))
              <= b + bounds[0] * gm[0] - eps * (1 - gm[1]))
        s.Add(gm[0] + gm[1] - 1 == delta)
    return delta


def reify(s, a, x, b, d=None, relation='<=', bounds=None, eps=1):
    # d == ` <--> a * x <= b
    return reify_raise(s, a, x, b, reify_force(s, a, x, b, d, relation, bounds),
                       relation, bounds, eps)


def solve_lady_or_tiger():
    s = new_solver('Lady or tiger', True)
    rooms = range(1, 10)  # There are 9 rooms
    # Decision variables
    # Given a set R = {1, 2, ..., 9} of rooms and a set B = {1, 2, 3} of beasts
    # 1 for empty, 2 for lady, and 3 for tiger
    R = [None] + [new_IntVar(s, 0, 2) for _ in rooms]
    S = [None] + [s.IntVar(0, 1, "") for _ in rooms]
    # Some constants to access the indicator variables of each room.
    i_empty, i_lady, i_tiger = 1, 2, 3
    # Ensure that there is exactly one lady
    k_out_of_n(s, 1, [R[i][i_lady] for i in rooms])
    for i in rooms:
        # If statement "i" is true, there is no tiger behind door i.
        reify_force(s, [1], [R[i][i_tiger]], 0, S[i], '<=')
        # A room with a lady has a true statement on its door
        reify_raise(s, [1], [R[i][i_lady]], 1, S[i], '>=')
    v = [1] * 5
    # R[1][i_lady]+R[3][i_lady]+R[5][i_lady]+R[7][i_lady]+R[9][i_lady] >= 1 reified at S[1]
    reify(s, v, [R[i][i_lady] for i in range(1, 10, 2)], 1, S[1], '>=')
    # “This room is empty” is a simple reification to S[2] of R[2][i_empty] >= 1
    reify(s, [1], [R[2][i_empty]], 1, S[2], '>=')
    # S[5] + (1-S[7]) >= 1 reified to S[3]
    reify(s, [1, -1], [S[5], S[7]], 0, S[3], '>=')
    # “Sign 1 is wrong.” is S[1]==0 reified to S[4]
    reify(s, [1], [S[1]], 0, S[4], '<=')
    # “Either sign 2 or sign 4 is right is reified to S[5]
    reify(s, [1, 1], [S[2], S[4]], 1, S[5], '>=')
    # "Sign 3 is wrong"
    reify(s, [1], [S[3]], 0, S[6], '<=')
    # “The lady is not in room 1.” needs to reify to S[7] the constraint R[1][i_lady] <= 0
    reify(s, [1], [R[1][i_lady]], 0, S[7], '<=')
    # "This room contains a tiger and room 9 is empty"
    reify(s, [1, 1], [R[8][i_tiger], R[9][i_empty]], 2, S[8], '>=')
    #  "This room contains a tiger and sign 6 is wrong"
    reify(s, [1, -1], [R[9][i_tiger], S[6]], 1, S[9], '>=')
    status = s.Solve()

    return status, [sol_val(S[i]) for i in rooms], [sol_val(R[i]) for i in rooms]


def main():
    # Solve the Lady or Tiger problem
    status, solution_S, solution_R = solve_lady_or_tiger()
    # Print the status of the solution
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution found:")
        # Display the solution for S[1..9] variables (whether signs are true/false)
        print("S values (signs):")
        for i in range(1, 10):
            print(f"S[{i}] = {solution_S[i - 1]}")
        # Display the solution for R[1..9] variables (room status: empty, lady, or tiger)
        print("\nRoom status (R):")
        for i in range(1, 10):
            empty, lady, tiger = solution_R[i - 1]
            print(f"Room {i}: Empty = {empty}, Lady = {lady}, Tiger = {tiger}")
    else:
        print("No optimal solution found.")


main()
