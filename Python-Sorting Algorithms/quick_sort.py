# This program implements Quick Sort
# Uses pivot + divide and conquer to sort the array
import numpy as np


def partition(a):  # Partition algorithm
    low = 0
    high = len(a) - 1
    pivot = a[high]
    i = low - 1  # Indicate the right position of pivot found so far
    for j in range(low, high):
        if a[j] < pivot:  # If the current value at index j is lower than pivot
            i += 1  # The "i" is incremented by 1
            a[i], a[j] = a[j], a[i]  # Swap index i and index j
    a[i + 1], a[high] = a[high], a[i + 1]  # Swap index i + 1 to the pivot
    return i + 1  # Return the correct position of the pivot


def quick_sort(a):  # [Time(n), Space(n) = O(n ^ 2), O(1)]
    low = 0
    high = len(a) - 1
    if low < high:
        pos = partition(a)
        # Divide the array into two parts, excluding the pivot
        # Recursively call the function will trigger partition again
        quick_sort(a[low:pos])
        quick_sort(a[pos+1:high+1])
    return a


def main():
    print("Quick Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = quick_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
