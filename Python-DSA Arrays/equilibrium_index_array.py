# Equilibrium index of an array
# the index that the sum of elements at lower indexes
# equals the sum of elements at higher indexes
import numpy as np


def equilibrium_point(arr):
    n = len(arr)
    # Check for indexes one by one until an equilibrium index is found
    for i in range(n):
        left_sum = sum(arr[:i])  # sum of elements before index i
        right_sum = sum(arr[i+1:])  # sum of elements after index i
        # If left_sum = right_sum, return the equilibrium index (1-based)
        if left_sum == right_sum:
            return i + 1
    # If no equilibrium index is found, return -1
    return -1


def main():
    print("Equilibrium index of an array")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(-10, 10, size=n)
    print("Array:", array)
    result = equilibrium_point(array)
    print("Equilibrium index:", result)


main()
