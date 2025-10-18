# Stock Buy and Sell – Multiple Transaction Allowed
# Calculating Maximum Profit
import numpy as np


def max_profit_rec(price, start, end):
    result = 0
    # Consider every valid pair, find the profit with it
    # and recursively find profits on left and right of it
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr = ((price[j] - price[i]) + max_profit_rec(price, start, i - 1)
                        + max_profit_rec(price, j + 1, end))
                result = max(result, curr)
    return result


# Wrapper function
def maximum_profit(prices):
    return max_profit_rec(prices, 0, len(prices) - 1)


def main():
    print("Stock Buy and Sell")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(1, 1000, size=n)
    print("Array:", array)
    max_profit = maximum_profit(array)
    print("Maximum Profit:", max_profit)


main()
