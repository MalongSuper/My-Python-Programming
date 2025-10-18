# This program solves Chocolate Distribution Problem
import numpy as np


def chocolate_distribution(arr, m):
    # Given an array of n integers
    # array[i]: Number of chocolates in the ith packet;
    # m: number of students
    n = len(arr)
    arr.sort()  # Sort the packets
    min_diff = float('inf')
    # Each student receives only one packet
    for i in range(n - m + 1):
        # The difference between the max and min number of chocolates
        # given to the students is minimized
        diff = arr[i + m - 1] - arr[i]
        # If current diff is smaller, update the min_diff
        if diff < min_diff:
            min_diff = diff
            print(arr[i: (i + m - 1) + 1])
    return min_diff


def main():
    print("Chocolate Distribution")
    # One example: array = [4, 3, 5, 42, 29, 16] and m = 3
    # We choose packets with {4, 3, 5} chocolates to distribute
    # With that, the diff = max - min = 5 - 3 = 2 is the smallest
    n = int(input("Enter size of the array: "))
    m = int(input("Enter number of students: "))  # m <= n
    array = np.random.randint(1, 50, size=n)
    print("Array:", array)
    print("Recommended distribution:")
    result = chocolate_distribution(array, m)
    print("Minimum difference:", result)


main()
