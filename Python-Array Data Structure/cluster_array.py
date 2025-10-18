# This program creates an array, then put the odd numbers on the left side
# And even numbers on the right side
# The order of the integers should be maintained
import numpy as np

print("Cluster Array")
size = eval(input("Enter the size of the array: "))
array = np.random.randint(0, 101, size=size)

print(f"Array before cluster: \n{array}")
# Indicate the array
odd_number = []
even_number = []
left = 0
right = len(array) - 1
while left <= right:
    if array[left] % 2 != 0:  # If odd number is found on the left side
        odd_number.append(array[left])
        left += 1
    # If not, it is an even number
    else:
        even_number.append(array[left])
        left += 1
# Combine the odd number list and even number list
array = odd_number + even_number
# Convert it to array
array = np.array(array)
print(f"Array after cluster: \n{array}")
