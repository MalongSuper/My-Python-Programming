# Knapsack Problem using Backtracking


def backtracking_approach(values, weights, max_weight, n, ci, cw, cv, sol, bes_sol, bes_val):
    if cw <= max_weight and cv > bes_val:
        bes_sol = sol.copy()
        bes_val = cv

    for i in range(ci, n):
        if cw + weights[i] <= max_weight:
            sol[i] = 1
            cw += weights[i]
            cv += values[i]
            bes_sol, bes_val = backtracking_approach(values, weights, max_weight,
                                                     n, i + 1, cw, cv, sol, bes_sol, bes_val)

            sol[i] = 0
            cw -= weights[i]
            cv -= values[i]

    return bes_sol, bes_val


def main():
    w_list = []
    v_list = []
    print("Knapsack Problem (Backtracking)")
    k = float(input("Enter weight of the bag: "))
    n = int(input("Enter the number of items: "))
    print("Weight")
    for i in range(1, n + 1):
        w = float(input(f"Enter w{i}: "))
        w_list.append(w)
    print("Value")
    for j in range(1, n + 1):
        v = float(input(f"Enter v{j}: "))
        v_list.append(v)

    solution = [0] * n
    best_solution = [0] * n
    best_value = 0
    best_solution, best_value = backtracking_approach(v_list, w_list,
                                                      k, n, 0, 0, 0, solution, best_solution, best_value)
    print("====================================")
    print("Chosen items:")
    for i in range(n):
        if best_solution[i] == 1:
            print(f"v{i + 1}: {v_list[i]}, w{i + 1}: {w_list[i]}")
    print(f"Maximum Value: {best_value}")


main()
