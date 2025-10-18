# Find the Missing Number in Arrays
import numpy as np
import random


def missing_number(n, arr):
    # Create hash array of size n+1
    hash_arr = [0] * (n + 1)
    # Store frequencies of elements
    for num in arr:
        hash_arr[num] += 1
    # Find the missing number
    for i in range(1, n + 1):
        if hash_arr[i] == 0:
            return i
    # Edge case handling
    return -1


def main():
    n = int(input("Enter size of the array: "))
    # Create an array from 1 to n
    array = np.arange(1, n)
    # Create a new array by removing one random element
    new_array = np.delete(array, random.randint(0, len(array) - 1))
    print("Array:", new_array)
    miss = missing_number(n, new_array)
    print("Missing elements:", miss)


main()
