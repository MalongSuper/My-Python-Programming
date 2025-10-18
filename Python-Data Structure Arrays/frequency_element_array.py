# This program finds the frequency of each element in array
import numpy as np

print("Frequency of elements in array")
size = eval(input("Enter the size of the array: "))
frequency = {}
array = np.random.randint(0, 101, size=size)
print(array)
# Use dictionary to find the frequency
for i in array:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# Display the result
for j, k in sorted(frequency.items()):
    print(f"The frequency of number {j}: {k}")
