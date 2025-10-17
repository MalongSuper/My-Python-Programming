# This program implements Comb Sort
import numpy as np


def comb_sort(a):  # Comb Sort [Time(n), Space(n) = O(n ^ 2), O(1)]
    n = len(a)
    gap = n
    is_sorted = False
    # If gap == 1 and the array is not sorted
    # The next iteration performs like Bubble Sort
    while (gap != 1) or (not is_sorted):
        gap = int(gap / 1.3)  # Shrink Factor = 1.3
        if gap <= 1:  # If gap is less than 1, treat it as gap = 1
            gap = 1
        # Use Bubble Sort for values that have gap
        is_sorted = True
        for i in range(0, n - gap, 1):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
                is_sorted = False  # The array is not yet sorted
    return a


def main():
    print("Comb Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = comb_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
