# This program sorts the elements based on their frequency
import numpy as np

print("Sort the elements based on their frequency ")
size = eval(input("Enter the size of the array: "))
array = np.random.randint(0, 101, size=size)
print(array)
frequency = {}

# Use dictionary to find the frequency
for i in array:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# Sort the keys based on the items in the dictionary
sorted_elements = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
sorted_elements = dict(sorted_elements)
# Take the key values as a list
key_elements = list(sorted_elements.keys())
# Display the list in array form
print("Array of elements are sorted based on their frequency:")
array = np.array(key_elements)
print(array)
