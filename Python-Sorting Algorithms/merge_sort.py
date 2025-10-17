# This program implements Merge Sort
# Divide the array to smaller parts then merge it back together
import numpy as np


def merge(left, right):  # Function to merge the array
    a = []
    n1 = len(left)
    n2 = len(right)
    i, j, k = 0, 0, 0
    while (i < n1) and (j < n2):
        if left[i] < right[j]:
            a.append(left[i])
            i += 1
            k += 1
        elif right[j] < left[i]:
            a.append(right[j])
            j += 1
            k += 1
        else:
            a.append(left[i])
            i += 1
            j += 1
            k += 1
    while i < n1:
        a.append(left[i])
        i += 1
        k += 1
    while j < n2:
        a.append(right[j])
        j += 1
        k += 1
    return a


def merge_sort(a):  # [Time(n), Space(n) = O(n log n), O(n)]
    if len(a) == 1 or len(a) == 0:  # If array has only one value or is empty
        return a
    else:
        low = 0
        high = len(a) - 1
        mid = (low + high) // 2
        left = merge_sort(a[:(mid + 1)])
        right = merge_sort(a[(mid + 1):])
        arr = merge(left, right)
        return arr


def main():
    print("Merge Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = merge_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
