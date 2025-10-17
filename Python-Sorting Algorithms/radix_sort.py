# This program implements Radix Sort
# Count the number of digits in the maximum element
import numpy as np


def radix_sort(a):  # [Time(n), Space(n) = O(n * d), O(n * d)]
    max_length = False
    temp, placement = -1, 1
    while not max_length:
        max_length = True
        # Create a bucket to store the numbers from index 0 to index 9
        buckets = [list() for _ in range(10)]  # Multi-dimensional List
        for i in a:
            temp = i // placement  # Take the number as temp
            # Find the digit of the number from last to first
            digit = temp % 10
            # Append the number to the array in the right index (based on digit
            buckets[digit].append(i)
            # If the length is maximum and no more temp
            if max_length and temp > 0:
                max_length = False
        # Initial Index
        v = 0
        for b in range(10):
            # Iterate through the bucket
            bucket = buckets[b]
            for i in bucket:
                a[v] = i  # Take the number in the bucket
                v += 1
        # Proceed to the next digit
        placement *= 10

    return a


def main():
    print("Radix Sort")
    number = int(input("Enter size of array: "))
    array = np.random.randint(1, 1000, size=number)
    print(f"Array: {array}")
    sorted_array = radix_sort(array)
    print(f"Sorted Array: {sorted_array}")


main()
