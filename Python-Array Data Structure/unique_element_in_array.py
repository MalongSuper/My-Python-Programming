# Given an array containing random numbers
# Find unique elements
import numpy as np


def find_unique_elements(arr):
    element_set = set()
    for num in arr:
        element_set.add(num)
    return element_set


def main():
    print("Find Unique Elements")
    size = int(input("Enter size of the array: "))
    array = np.random.randint(1, 20, size=size)
    print("Array:", array)
    result = find_unique_elements(array)
    print(f"Unique Elements: {" ".join(str(n) for n in result)}")


main()
