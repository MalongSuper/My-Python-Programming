# This program implements Insertion Sort
# Divide into two arrays, compare the elements in each array and shift them
import numpy as np


def insertion_sort(a):  # Insertion Sort [Time(n), Space(n) = O(n ^ 2), O(1)]
    n = len(a)
    # left: The left array with the elements sorted
    # right: The right array uses for shifting elements
    # Temp: Store the element of the right array
    for right in range(1, n, 1):  # Start from index 1
        temp = a[right]
        left = right - 1
        while left >= 0 and a[left] > temp:
            # Shift the element to the right to perform replacement
            a[left + 1] = a[left]
            left -= 1
        a[left + 1] = temp  # Right position found
    return a


def main():
    print("Insertion Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = insertion_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
