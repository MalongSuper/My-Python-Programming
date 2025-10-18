# This program implements Linear Search algorithm
import numpy as np


def linear_search(arr, k):  # Linear Search
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    # The element is not found
    return False


def main():
    print("Linear Search")
    n = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=n)
    print("Array:", array)
    key = int(input("Enter the number you want to search: "))
    # Implement linear search
    i = linear_search(array, key)
    if i:
        print(f"=> The element is at index {i}")
    else:
        print(f"=> The element is not present")


main()
