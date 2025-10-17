# Odd-Even Sorting
# Each iteration has two phases, phase 1: Sort the odd indexed elements
# phase 2: Sort the even indexed elements using Bubble Sort
import numpy as np


def odd_even_sort(a):  # Time Complexity: O(N^2)
    n = len(a)
    for i in range(n):  # Iterate through array
        is_sorted = True
        for j in range(1, n - 1, 2):  # Compare and swap the odd indexed elements
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sorted = False  # The array is not yet sorted
        for j in range(0, n - 1, 2):  # Compare and swap the even indexed elements
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sorted = False  # The array is not yet sorted
        if is_sorted:   # If the array is already sorted
            break
    return a


def main():
    print("Odd-Even Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = odd_even_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
