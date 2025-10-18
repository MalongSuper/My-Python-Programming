# This program finds intersection of two arrays
# Elements that are present in both arrays
import numpy as np


def intersection(a, b):
    result = []
    # Traverse through a[] and search every element a[i] in b[]
    for i in a:
        for j in b:
            # If found, check if the element is already in the result
            if i == j and i not in result:
                result.append(i)
    return result


def main():
    print("Intersection of two arrays")
    m = int(input("Enter size of the array 1: "))
    n = int(input("Enter size of the array 2: "))
    array1 = np.random.randint(0, 20, size=m)
    array2 = np.random.randint(0, 20, size=n)
    print("Array 1:", array1)
    print("Array 2:", array2)
    result = intersection(array1, array2)
    print("Intersection Array:", np.array(result))


main()
