# 0/1 Knapsack Problem using Dynamic Programming (Bottom-Up Approach)


def knapsack_dp(values, weights, capacity):
    n = len(values)
    table = [[0]*(capacity + 1) for y in range(n + 1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                include_item = values[i-1] + table[i-1][w-weights[i-1]]
                exclude_item = table[i-1][w]
                table[i][w] = max(include_item, exclude_item)
            else:
                table[i][w] = table[i-1][w]
    
    for row in table:
        print(row)
    return table[n][capacity]


def main():
    w_list = []
    v_list = []
    print("Knapsack Problem (Dynamic Programming Approach)")
    k = int(input("Enter the bag weight: "))
    n = int(input("Enter number of items: "))
    print("Weight")
    for i in range(1, n + 1):
        w = int(input(f"Enter w{i}: "))
        w_list.append(w)
    print("Value")
    for j in range(1, n + 1):
        v = int(input(f"Enter v{j}: "))
        v_list.append(v)
    result = knapsack_dp(v_list, w_list, k)
    print("Maximum Value in Knapsack:", result)


main()