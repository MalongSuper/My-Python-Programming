# Knapsack Problem: First Approach
# Not Genetic Algorithm
import random

# Fitness Function: Maximize the Profit while ensuring the number of items do not exceed the weight
items = [[7, 5], [2, 4], [1, 7], [9, 2], [5, 1], [3, 3]]
capacity = 15
generations = 100
included_items = []
profits = []


for j in range(generations):
    print(f"Generation {j + 1}")
    random_genome = [random.choice([0, 1]) for _ in range(len(items))]
    print(random_genome)
    for i in range(len(items)):
        if random_genome[i] == 0:
            included_items.append(0)
            profits.append(0)
        if random_genome[i] == 1:
            included_items.append(items[i][0])
            profits.append(items[i][1])

    total_items, total_profits = sum(included_items), sum(profits)

    print("Included Items:", included_items)
    print("Profits:", profits)
    print("Total Items:", total_items)
    print("Total Profits:", total_profits)

    if total_items <= total_items < capacity:
        print("Optimal Solution Found!!")
        break

    # Reset to original state
    included_items = []
    total_profits = []
