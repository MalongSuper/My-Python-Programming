# This program implements Counting Sort
# Counts the occurrence of an element in the input array
import numpy as np


def counting_sort(a):  # [Time(n), Space(n) = O(n + k), O(k)]
    # Create a count array
    max_array = max(a)
    count_array = [0] * max_array
    # Count the occurrence of each element in array
    for i in a:
        # Store them in the count array based on index
        count_array[i - 1] += 1
    # Iteratively compute the elements closest to each other in array
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    # Construct the sort array
    sort_array = [0] * len(a)
    for k in range(len(a) - 1, -1, -1):
        # Shift the computed occurrence
        sort_array[count_array[a[k] - 1] - 1] = a[k]
        count_array[a[k] - 1] -= 1

    return sort_array


def main():
    print("Counting Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=number)
    print(f"Array: {array}")
    sorted_array = counting_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
