# This program implements Selection Sort
# Compare the first element with the remaining elements from the 2nd onwards
import numpy as np


def selection_sort(a):  # Selection Sort [Time(n), Space(n) = O(n ^ 2), O(1)]
    n = len(a)
    for i in range(0, n - 1, 1):
        # Suppose the element at index i is the min value, flag it
        flag = i
        for j in range(i + 1, n, 1):
            # Find the minimum element and flag it
            if a[j] < a[flag]:  # current element < the flag element
                flag = j
        # Rotate the current element with the ith element
        a[i], a[flag] = a[flag], a[i]
    return a


def main():
    print("Selection Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = selection_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
