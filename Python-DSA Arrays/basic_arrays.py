# Create basic arrays
import numpy as np

# Create an array from list
array1 = np.array(([1, 2, 3, 4], [1, 3, 4, 5]))
print("Array 1:\n", array1)
print("len =", len(array1))  # Length of array
print("len =", array1.shape)  # Shape of the array
# Create a 2D array 3x4 with zeros
array2 = np.zeros((3, 4))
print("Array 2:\n", array2)
# Create a 2D array 3x4 with ones
array3 = np.ones((3, 4))
print("Array 3:\n", array3)
# Create a 2D array 3x4 with fives
array4 = 5 * np.ones((3, 4))
print("Array 4:\n", array4)
# Create an array with values from 0 to 10
array5 = np.arange(0, 10)  # Different by 1
print("Array 5:\n", array5)
array6 = np.arange(0, 10, 2)  # Different by 2
print("Array 6:\n", array6)
# An array with 6 values, start from 0 and stop to 10
array7 = np.linspace(0, 10, 6)
print("Array 7:\n", array7)
# Create an array then reshape it
array8 = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 4)
print("Array 8:\n", array8)
# Create a 2D array 3x4 with diagonal = 1
array9 = np.eye(3, 4)
print("Array 9:\n", array9)
# Create an identity matrix
array10 = np.identity(3)
print("Array 10:\n", array10)
# Create a matrix of only fives
array11 = np.full((3, 3), 5)
print("Array 11:\n", array11)
# Create a random matrix
array12 = np.random.randint(0, 10, (3, 4))
print("Array 12:\n", array12)
