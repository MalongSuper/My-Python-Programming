# Single element among doubles
# All numbers occur more than twice
# except one number which occurs once
import random


def find_single(arr):
    # Iterate over every element
    for i in arr:
        # Initialize count to 0
        count = 0
        for j in arr:
            # Count the frequency of the element
            if i == j:
                count += 1
        # If the frequency of the element is one
        if count == 1:
            return i
    # If no element exists at most once
    return -1


def main():
    print("Single element among doubles")
    n = int(input("Enter size of the initial array: "))
    # Generate an array that every element occurs more than twice
    # Except one
    init_array = []
    for i in range(n):
        e = random.randint(0, 30)
        init_array.append(e)
    array = init_array + init_array  # Merge two arrays
    array.pop(random.randint(0, len(array) - 1))
    print("Array:", array)
    result = find_single(array)
    print("Single element:", result)


main()
