# This is finds all the elements greater than the mean of the elements.
import numpy as np
number_list = []
better_list = []
print("Elements greater than the mean of the elements")
number = int(input("Enter number of elements: "))
array = np.random.randint(0, 101, size=number)
print("Array:", array)
# Compute the mean (average)
mean = sum(array) / len(array)
print("Mean:", int(mean))
# Find the greater elements
print(f"All greater elements in array: ", end="")
for j in array:
    if j > mean:
        better_list.append(j)
print(', '.join(map(str, better_list)))
