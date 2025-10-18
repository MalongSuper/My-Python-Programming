# Basic Indexing and Slicing in Array
import numpy as np
import random
print("Indexing and Slicing in Array")
n, m = eval(input("Enter size of the array: "))
# Array with elements ranging from 0 to n
array1 = np.arange(0, n)
print("Array1 =", array1)
# Slicing and Indexing
index1, index2 = random.randint(0, len(array1) // 2), random.randint(len(array1) // 2, len(array1) - 1)
print("Array1[:] =", array1[:])
print(f"Array1[{index1}: {index2}] =", array1[index1:index2])
# Array with random elements with n size
array2 = np.random.randint(1, 100, size=(n, m))
index1, index2 = random.randint(0, len(array2) // 2), random.randint(len(array2) // 2, len(array2) - 1)
print("Array2 =\n", array2)
print("Array2[:] =\n", array1[:])
print(f"Array2[{index1}: {index2}] =\n", array2[index1:index2])
array2 = array2.copy()  # Copy the original array
print(f"Array2[{index1}][{index2}] =\n", array2[index1][index2])
