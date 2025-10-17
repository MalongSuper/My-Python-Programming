# This program implements Bubble Sort
import numpy as np


def bubble_sort(a):  # Bubble Sort [Time(n), Space(n) = O(n ^ 2), O(1)]
    n = len(a)
    for i in range(1, n, 1):  # Iterate through array
        is_sorted = True
        # Compare all couple of nearest numbers
        # The lower number is rotated to the left side of the array
        for j in range(0, n - i, 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sorted = False  # The array is not yet sorted
        if is_sorted:   # If the array is already sorted
            break
    return a


def main():
    print("Bubble Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = bubble_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
