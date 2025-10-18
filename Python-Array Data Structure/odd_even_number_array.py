# Create an array
# Compute all elements at odd index and all elements at even index
import numpy as np
import random
odd_list, even_list = [], []
number_list = []
print("Odd and Even numbers in Array")
n = int(input("Enter size of array: "))
for i in range(n):
    number = random.randint(1, 100)
    number_list.append(number)
# Create an array
array = np.array(number_list)
print("Array:", array)
for j in range(len(number_list)):
    if j % 2 == 0:  # Add elements at the even index to even list
        even_list.append(number_list[j])
    else:  # Add elements at the odd index to odd list
        odd_list.append(number_list[j])
# Display the result
print("Sum of even index:", sum(even_list))
print("Sum of odd index:", sum(odd_list))
