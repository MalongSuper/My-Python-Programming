# This program finds Maximum Product Subarray
# using nested loops
import numpy as np


def max_product(arr):
    n = len(arr)
    result = arr[0]  # Initial result
    for i in range(n):
        multi = 1
        # traversing in current subarray
        for j in range(i, n):
            multi *= arr[j]
            # updating result every time
            # to keep track of the maximum product
            result = max(result, multi)
    return result


def main():
    print("Maximum Sub-array Product")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(0, 50, size=n)
    print("Array:", array)
    result = max_product(array)
    print("Product of maximum subarray", result)


main()
