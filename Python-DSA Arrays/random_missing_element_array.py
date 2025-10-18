# This program displays an (n - 1) array with a random missing element
# The program should find the missing number
# Suggests three solutions
import numpy as np
import random
print("Find missing number in array")
n = int(input("Enter n: "))
my_list = [i for i in range(1, n)]
# One element will be missing in list
random_element = random.randrange(0, len(my_list))
# The missing element will be 0
my_list[random_element] = 0
# Convert to array
array = np.array(my_list)
print(array)

# Solution 1: Using iteration
print("Solution 1: Iteration")
missing_number = None
for j in range(1, n):
    if j not in array:
        missing_number = j
        break
print("Missing number is", missing_number)


# Solution 2: Using Set
print("Solution 2: Set")
number_set = set(range(1, n))
missing_number = number_set - set(array)
print("Missing number is", missing_number.pop())


# Solution 3: Using Dictionary
print("Solution 3: Dictionary")
number = {}
for num in array:
    if num in number:
        number[num] += 1
    else:
        number[num] = 1

missing_number = None
for num in range(1, n):
    if num not in number:
        missing_number = num
        break
print("Missing number is", missing_number)
