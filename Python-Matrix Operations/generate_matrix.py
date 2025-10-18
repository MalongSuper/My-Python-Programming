# Generate Matrix
import numpy as np
print("Generate Matrix")
m, n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(m, n))
print(matrix)
