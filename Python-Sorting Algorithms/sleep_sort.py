# Sleep Sort implementation
import time
import numpy as np


def sleep_sort(a):  # Time Complexity: Somewhat O(max(array) + n)
    max_value = max(a)  # Take the max value
    n = len(a)
    second = 0
    sorted_array = []
    for i in range(0, max_value + 1):
        # The program sleeps for every 1 second
        second += 1
        print(f"Sleep for {i} seconds")
        time.sleep(1)
        for j in range(n):
            if a[j] == i:  # Find the element in the array
                # with the corresponding number and append it
                sorted_array.append(a[j])
    return sorted_array


def main():
    print("Sleep Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(0, 120, size=number)
    print(f"Array: {array}")
    sorted_array = sleep_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
