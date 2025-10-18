# This program finds the maximum subarray sum
# using nested loops
import numpy as np


def max_subarray_sum(arr):
    n = len(arr)
    result = arr[0]  # Initial result
    # Outer loop for starting point of subarray
    for i in range(n):
        current_sum = 0
        # Inner loop for ending point of subarray
        for j in range(i, n):
            current_sum = current_sum + arr[j]
            # Update res if currSum is greater than res
            result = max(result, current_sum)
    return result


def main():
    print("Maximum Sub-array Sum")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(0, 50, size=n)
    print("Array:", array)
    result = max_subarray_sum(array)
    print("Sum of maximum subarray:", result)


main()
