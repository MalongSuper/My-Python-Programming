# This program implements Binary Search
# Using Divide and Conquer & Recursion algorithm
import numpy as np


def binary_search(arr, low, high, k):  # Binary Search
    if low > high:
        return False  # Base case: element not found
    mid = (low + high) // 2
    if arr[mid] == k:
        return mid  # Element found
    elif arr[mid] > k:
        return binary_search(arr, low, mid - 1, k)  # Search in the left half
    else:
        return binary_search(arr, mid + 1, high, k)  # Search in the right half


def main():
    print("Binary Search")
    n = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=n)
    array.sort()
    print("Array:", array)
    key = int(input("Enter the number you want to search: "))
    # Implement binary search
    i = binary_search(array, 0, len(array) - 1, key)
    if i:
        print(f"=> The element is at index {i}")
    else:
        print(f"=> The element is not present")


main()
