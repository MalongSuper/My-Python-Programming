# Diet Problem Mixing types (Linear Continuous Models)
# Fi: foods; Ni: nutritional content; Min (Li), Max (Ui): number of servings
# Cost (Ci): cost of each food
# a: Maximum nutritional content; b: Minimum nutritional content
# Select the set of foods that will satisfy
# a set of daily nutritional requirement at minimum cost.
from ortools.linear_solver import pywraplp
import numpy as np


# N 2-dimensional matrix (table) contains the food and its nutrition
def solve_diet(n):
    solver = pywraplp.Solver("Diet Problem",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # Decision variables
    # fi: number of servings of each food
    n_foods = len(n) - 2  # Exclude the last two rows
    # ni: nutritional content of each food
    n_nutrients = len(n[0]) - 3  # Exclude the last three cols
    # The position of MinServing (l), MaxServing (u), Cost for one portion
    f_min, f_max, f_cost = n_nutrients, n_nutrients + 1, n_nutrients + 2
    # The position of MinNutrient (a), MaxNutrient (b) for one portion
    n_min, n_max = n_foods, n_foods + 1
    # f is an array with the decision variable in range [l, u]
    f = [solver.NumVar(n[i][f_min], n[i][f_max], 'f[%i]' % i)
         for i in range(n_foods)]
    print("Number of variables =", solver.NumVariables())
    # Constraints
    # The number of servings selected (called fi) must not exceed
    # the min and max servings for each food
    # Thus,the sum of the product of fi and the nutritional content
    # of each food must not exceed the nutritional content capacity
    for j in range(n_nutrients):
        solver.Add(solver.Sum([f[i] * n[i][j]
                               for i in range(n_foods)]) >= n[n_min][j])
        solver.Add(solver.Sum([f[i] * n[i][j]
                               for i in range(n_foods)]) <= n[n_max][j])
    print("Number of constraints =", solver.NumConstraints())
    # Objective: Minimum cost sigma(fi * ci)
    solver.Minimize(solver.Sum(f[i] * n[i][f_cost]
                               for i in range(n_foods)))
    status = solver.Solve()
    # Return an array with optimal value of decision variables f[i]
    if status == solver.OPTIMAL:
        return [f[i].solution_value() for i in range(n_foods)]
    elif status != solver.OPTIMAL:
        print("This problem does not have an optimal solution!")
        if status == solver.FEASIBLE:
            print("A potentially suboptimal solution was found.")
        else:
            print("The solver could not solve the problem.")
        return None


def main():
    # The matrix contains the N0, N1, N2, N3, Min, Max, Cost for each food (Fi)
    # The last two rows contain Min/Max of nutrients
    N = [[606, 563, 665, 23, 7, 17, 9.06],
         [68, 821, 83, 72, 6, 27, 8.42],
         [28, 70, 916, 56, 1, 36, 9.47],
         [121, 429, 143, 38, 14, 26, 6.97],
         [60, 179, 818, 46, 9, 35, 4.77],
         [5764, 28406, 48157, 1642, ],
         [15446, 76946, 82057, 6280, ]]
    fi = solve_diet(N)
    print("Serving of each food:\n", fi)
    # Calculate the nutritional content
    x = len(N) - 2
    solution_list = []
    array = np.array(N[0:x])  # Create an array (exclude the last 2rows and the last 3 cols)
    for i in range(len(array) - 1):
        for j in range(len(array[:, i])):
            res = fi[j] * array[:, i][j]  # fi * Ni
            solution_list.append(res)  # Append to list
    # Convert to array, reshape to 5x5 matrix
    solution = np.array(solution_list).reshape(4, 5)
    for k in range(len(solution)):  # Calculate the sum
        print(f"Solution N{k}: {np.sum(solution[k])}")


main()
