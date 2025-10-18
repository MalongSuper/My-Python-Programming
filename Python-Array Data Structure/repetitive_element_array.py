# Find element that only repeats from 1 to n - 1
import numpy as np


def find_repeating(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]
    return -1


def main():
    n = int(input("Enter size of the array: "))
    array = np.random.randint(1, 9, size=n)
    print("Array:", array)
    rep = find_repeating(array)
    print("Repeated element:", rep)


main()
