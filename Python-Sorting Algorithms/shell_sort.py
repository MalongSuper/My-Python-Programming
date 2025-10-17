# This program implements Shell Sort
import numpy as np


def shell_sort(a):  # [Time Complexity: O(n^2); Space Complexity: O(1)]
    n = len(a)
    # Rearrange elements at each n/2, n/4, n/8, ..., 1 interval
    interval = n // 2  # Initialize the interval by length // 2
    while interval > 0:
        for i in range(interval, n):
            temp = a[i]
            j = i
            while j >= interval and a[j - interval] > temp:
                # Assign a[j] to a[j - interval]
                a[j] = a[j - interval]
                j -= interval
            a[j] = temp
        interval = interval // 2  # Reduce the interval
    return a


def main():
    print("Shell Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(0, 120, size=number)
    print(f"Array: {array}")
    sorted_array = shell_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
