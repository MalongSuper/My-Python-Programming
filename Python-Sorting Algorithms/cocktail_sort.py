# This program implements Cocktail Sort
# Reference: W3resource
import numpy as np


def cocktail_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        is_swapped = False
        for j in range(i, 0, -1):  # Visit the sequence from right to left
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                is_swapped = True
        for j in range(i):  # Visit the sequence from left to right
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_swapped = True
        if not is_swapped:  # If there is no swap in the entire iteration
            return a  # The array is sorted


def main():
    print("Cocktail Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(0, 120, size=number)
    print(f"Array: {array}")
    sorted_array = cocktail_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
