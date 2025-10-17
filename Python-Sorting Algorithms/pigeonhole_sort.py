# This program implements Pigeonhole Sort
# Reference: https://www.geeksforgeeks.org/python-program-for-pigeonhole-sort/
import numpy as np


def pigeonhole_sort(a):
    n = len(a)
    # Find the size of range by (max - min + 1)
    min_value, max_value = min(a), max(a)
    size = max_value - min_value + 1
    # Create a list of pigeonholes of size
    holes = [0] * size
    # Traverse through the array and put the value
    # into its pigeonhole
    for x in a:
        holes[x - min_value] += 1
    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + min_value
            i += 1
    return a


def main():
    print("Pigeonhole Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(0, 120, size=number)
    print(f"Array: {array}")
    sorted_array = pigeonhole_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
