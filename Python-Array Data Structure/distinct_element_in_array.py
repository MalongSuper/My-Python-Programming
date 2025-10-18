# This program returns all distinct element in an array
import numpy as np


def find_distinct(arr):
    result = []
    for i in range(len(arr)):
        # Check if this element is included in result
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                break
            j += 1
        # Include this element if not included previously
        if i == j:
            result.append(arr[i])

    return result


def main():
    print("Distinct Elements in Array")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(1, 50, size=n)
    print("Array:", array)
    result = find_distinct(array)
    print("Distinct elements:", end=" ")
    for val in result:
        print(val, end=" ")


main()
