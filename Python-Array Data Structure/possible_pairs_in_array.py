# This program finds all possible pairs of numbers in the array
# Which have the sum equal to the given value
import numpy as np


def find_pairs_of_numbers(arr, target_value):
    pairs_of_number = []
    # Sort the array in ascending order
    arr.sort()
    left = 0  # First index on the list (Left side)
    right = len(arr) - 1  # Last index on the list (Right side)
    while left <= right:
        # Sum the elements based on the index indicated
        current_sum = arr[left] + arr[right]
        if current_sum == target_value:  # If it is equal to the target value
            pairs_of_number.append((arr[left], arr[right]))
            # Proceed to the next index
            left += 1
            right -= 1
        elif current_sum < target_value:
            left += 1
        else:
            # The possible case is current_sum > target_value
            right -= 1
    return pairs_of_number


print("Possible pairs of number in array")
size = int(input("Enter the size of the array: "))
array = np.random.randint(0, 101, size=size)
print(array)
value = int(input("Enter a value: "))
pairs = find_pairs_of_numbers(array, value)
if not pairs:
    print("No pairs of numbers found")
else:
    print("Possible pairs of numbers:")
    for p in pairs:
        print(p, end=" ")
