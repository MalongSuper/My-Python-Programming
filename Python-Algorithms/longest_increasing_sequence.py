# Find LIS - Longest Increasing Sequence (Stalin Sort)
# Useful for filtering incorrect data
import numpy as np


def stalin_sort(a):
    n = len(a)
    if n == 1:  # If the array only has one element, return it
        return a
    result = [a[0]]  # Start with the first element in rhe array
    for i in range(1, n):
        if a[i] >= result[-1]:  # If current element is greater than
            # or equal to the last element in result
            result.append(a[i])  # Add it to the result
    return result


def main():
    print("Longest Increasing Sequence (Stalin Sort)")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 50, size=number)
    print(f"Array: {array}")
    sorted_array = stalin_sort(list(array))
    print(f"Sorted Array: {sorted_array}")


main()
