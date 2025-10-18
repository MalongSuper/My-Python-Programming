# This program sort an array in wave form
# arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
import numpy as np


def sort_in_wave(arr, n):
    # sort the array
    arr.sort()
    # Swap adjacent elements
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


def main():
    print("Sort array in wave form")
    n = int(input("Enter size of the array: "))
    array = np.random.randint(0, 50, size=n)
    print("Array:", array)
    sort_in_wave(array, len(array))
    print("Wave Array: ", end="")
    for i in range(0, len(array)):
        print(array[i], end=" ")


main()
