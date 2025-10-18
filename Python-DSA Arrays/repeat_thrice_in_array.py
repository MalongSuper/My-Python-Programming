# Given an array of random numbers
# find if any number is repeated thrice or more
import numpy as np


def find_thrice(arr):  # Function to find the number that repeats thrice
    num_list = []
    count_map = {}  # Use a dictionary
    # Count occurrence of each number in array
    for num in arr:  # A dictionary will be created
        # Keys are numbers in the array, Items are set to 1 as default
        if num in count_map:
            count_map[num] += 1  # Add 1 count as the item of the key
        else:
            count_map[num] = 1  # The item to the key stays as 1
    # Check if any number has occurred more than three times
    for num, count in count_map.items():
        if count >= 3:
            num_list.append(int(num))
    # Display the list of numbers
    if len(num_list) > 0:
        return sorted(num_list)
    else:
        return None


def main():
    print("Find number repeated thrice or more in array")
    size = int(input("Enter size of the array: "))
    array = np.random.randint(1, 20, size=size)
    print("Array:", array)
    result = find_thrice(array)
    if result is not None:
        print(f"Numbers repeated more than thrice: {" ".join(str(n) for n in result)}")
    else:
        print(f"No number repeated more than thrice")


main()
