# Display and Reverse Array
import numpy as np
import random
# Create list with random values
number_list = []
print("Reverse Array")
n = int(input("Enter size of array: "))
for i in range(n):
    number = random.randint(1, 100)
    number_list.append(number)
# Create an array
array = np.array(number_list)
print("Array:", array)
print("Reversed Array:", array[::-1])
