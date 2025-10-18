# Union of two arrays
# Merging elements from two arrays, excluding duplicates
import numpy as np


def find_union(a, b):
    result = []
    # Traverse through a[] and search every element
    # a[i] in result
    for i in range(len(a)):
        # check if the element is already
        # in the result to avoid duplicates
        j = 0
        while j < len(result):
            if result[j] == a[i]:
                break
            j += 1
        if j == len(result):
            result.append(a[i])
    # Traverse through b[] and search every element
    # b[i] in result
    for i in range(len(b)):
        # check if the element is already
        # in the result to avoid duplicates
        j = 0
        while j < len(result):
            if result[j] == b[i]:
                break
            j += 1
        if j == len(result):
            result.append(b[i])
    return result


def main():
    print("Union of two arrays")
    m = int(input("Enter size of the array 1: "))
    n = int(input("Enter size of the array 2: "))
    array1 = np.random.randint(0, 20, size=m)
    array2 = np.random.randint(0, 20, size=n)
    print("Array 1:", array1)
    print("Array 2:", array2)
    result = find_union(array1, array2)
    print("Union Array:", np.array(result))


main()
