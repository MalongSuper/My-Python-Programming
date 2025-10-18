# Solve Knapsack Problem using Greedy Approach
def greedy_approach(values, weights, max_weight):
    total_value = 0
    chosen_items = []
    # Sort the values using the vi/wi ratio
    items = sorted(zip(values, weights, range(len(values))), key=lambda x: x[0]/x[1], reverse=True)
    # Find the maximum total value
    for v, w, i in items:
        if max_weight >= w:
            max_weight -= w
            total_value += v
            chosen_items.append(i)
        else:
            total_value += max_weight * (v / w)
            chosen_items.append(i)
            break
    total_value = round(total_value, 1)
    return total_value, chosen_items


def main():
    w_list = []
    v_list = []
    print("Knapsack Problem (Greedy Approach)")
    k = float(input("Enter the bag weight: "))
    n = int(input("Enter number of items: "))
    print("Weight")
    for i in range(1, n + 1):
        w = float(input(f"Enter w{i}: "))
        w_list.append(w)
    print("Value")
    for j in range(1, n + 1):
        v = float(input(f"Enter v{j}: "))
        v_list.append(v)
    max_value, chosen_items = greedy_approach(v_list, w_list, k)
    print("====================================")
    print(f"Maximum Value: {max_value}")
    print(f"Chosen items: ")
    for d in chosen_items:
        print(f"w{d + 1}", end=" ")


main()
