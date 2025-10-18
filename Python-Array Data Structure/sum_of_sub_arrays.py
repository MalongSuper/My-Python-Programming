# Sum of all Sub-arrays
import numpy as np


def sum_subarrays(arr):
    temp, result = 0, 0
    n = len(arr)
    # Starting point
    for i in range(0, n):
        # Ending point
        temp = 0
        for j in range(i, n):
            # Sum sub-array between current starting and ending points
            temp += arr[j]
            result += temp
    return result


def main():
    print("Sum of Sub-Arrays")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(1, 50, size=n)
    print("Array:", array)
    result = sum_subarrays(array)
    print("Sub-Arrays Sum:", result)


main()
