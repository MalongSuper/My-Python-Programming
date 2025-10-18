# Sudoku Problem (Possible solutions)
import numpy as np
from ortools.linear_solver import pywraplp


def solve_sudoku(grid_size, m):
    # Create solver
    solver = pywraplp.Solver.CreateSolver("SCIP")
    # Decision variables
    sudoku_vars = np.empty((grid_size, grid_size, grid_size), dtype=object)
    for row in range(grid_size):
        for col in range(grid_size):
            for num in range(grid_size):
                sudoku_vars[row][col][num] = solver.Var(0, 1, integer=True,
                                                        name=f"x_{row, col, num}")
    # Objective Functions
    solver.Minimize(0)
    # Constraints
    # Row of the sudoku board must be within 1 to 9
    for row in range(grid_size):
        for num in range(grid_size):
            solver.Add(solver.Sum([sudoku_vars[row][col][num]
                                   for col in range(grid_size)]) == 1)
    # Column of the sudoku board must be within 1 to 9
    for col in range(grid_size):
        for num in range(grid_size):
            solver.Add(solver.Sum([sudoku_vars[row][col][num]
                                   for row in range(grid_size)]) == 1)
    # 9x9 Grid of the sudoku board must be within 1 to 9
    for row in range(grid_size):
        for col in range(grid_size):
            solver.Add(solver.Sum([sudoku_vars[row][col][num]
                                   for num in range(grid_size)]) == 1)
    # Each number in each row, col in the board only appears one time
    for row in range(grid_size):
        known_values = m[row]
        for value in known_values:
            row, col, num = value
            solver.Add(sudoku_vars[row - 1][col - 1][num - 1] == 1)
    # Solve the problem
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        sudoku_sol = np.zeros((grid_size, grid_size), dtype=int)
        for row in range(grid_size):
            for col in range(grid_size):
                for num in range(grid_size):
                    if sudoku_vars[row][col][num].solution_value() == 1:
                        sudoku_sol[row][col] = num + 1
        return sudoku_sol
    else:
        return None


grid_size = 9
subgrid_size = 3
M = [[(1, 3, 6)],
     [(2, 3, 3)],
     [(3, 1, 5), (3, 7, 3), (3, 8, 7), (3, 9, 9)],
     [(4, 1, 2), (4, 2, 1), (4, 3, 4), (4, 4, 0)],
     [(5, 6, 5), (5, 7, 4)],
     [(6, 1, 3), (6, 2, 5), (6, 3, 8), (6, 7, 9)],
     [(7, 1, 4), (7, 9, 2)],
     [(8, 3, 5)],
     [(9, 1, 8), (9, 2, 2)]]
# Display the result
solution = solve_sudoku(grid_size, M)
if solution is not None:  # However, not the right solution
    print(solution)
