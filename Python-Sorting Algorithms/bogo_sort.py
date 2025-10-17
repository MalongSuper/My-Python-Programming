# Bogo Sort (or Permutation Sort)
# Randomly shuffling the sequence until the sorted sequence is found
import random
import time
import numpy as np


def permutation(a, left, right):
    result = []  # List to store all the permutations
    if left == right:
        # Append a copy of the list (to avoid reference issues
        result.append(a[:])
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]  # Swap
            # Recursively collect permutations
            result += permutation(a, left + 1, right)
            a[left], a[i] = a[i], a[left]  # Backtrack (restore the list)
    return result


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def bogo_sort(arr):  # Time Complexity: Somewhat O(n!) or O(n!^2)
    # The normal algorithm takes the time complexity of O(infinity)
    # Here, we can improve this algorithm by:
    # + Generating all the possible permutations of the sequence
    # + Randomize one of them, and if it is not the resultant sequence
    # + Remove them from the list
    permute_list = permutation(arr, 0, len(arr) - 1)
    while not is_sorted(arr):
        arr = random.choice(permute_list)
        permute_list.remove(arr)
    return arr


def main():
    print("Bogo Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(-20, 20, size=number)
    print(f"Array: {array}")
    # Using the Bogo Sort approach
    start = time.time()
    sorted_array = bogo_sort(list(array))
    end = time.time()
    print(f"Sorted Array: {sorted_array}")
    print(f"+ Time: {end - start}")


main()
