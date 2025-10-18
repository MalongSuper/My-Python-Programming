# Rearrange array
# such that even positioned are greater than odd
import numpy as np


def assign(arr):
    n = len(arr)
    # Sort the array
    arr.sort()
    ans = [0] * n
    # Two pointers point at the first and the last index
    ptr1 = 0
    ptr2 = n - 1
    for i in range(n):
        # Assign even indexes with maximum elements
        if i % 2 == 1:
            ans[i] = arr[ptr2]
            ptr2 = ptr2 - 1
        # Assign odd indexes with remaining elements
        else:
            ans[i] = arr[ptr1]
            ptr1 = ptr1 + 1
    # Display result
    for i in range(n):
        print(ans[i], end=" ")


def main():
    print("Rearrange Array (even index > odd index)")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(1, 50, size=n)
    print("Array:", array)
    assign(array)


main()
