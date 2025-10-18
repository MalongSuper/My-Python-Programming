# Fake Coin Problem
import numpy as np


# Return the weight of the coin
def weight(coins, i, j):
    weight = 0
    for k in range(i, j):
        weight += coins[k]
    return weight


# Find the single possible fake coin in the array from i to j
def fake_coin(coins, i, j):
    if i == (j - 1):
        print("The fake coin is at position:", i)
        return i

    # Continue split if no fake coin is found yet
    m = (i + j) // 2
    # If the weights between two groups are different
    # The fake coin is in one of the two groups
    if weight(coins, i, m) != weight(coins, m, j):
        fake_coin(coins, i, m)
        fake_coin(coins, m, j)
    return None


def main():
    coins = 3.4 * np.ones(16)  # 16 coins with weight 3
    coins[3] = 2.8  # Coin at index 3 has different weight
    print("Coins:\n", coins)
    fake_coin(coins, 0, len(coins))


main()
