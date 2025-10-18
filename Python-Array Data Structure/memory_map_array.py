# Memory Map for an array
import numpy as np
import random
from tempfile import mkdtemp
import os.path as os_path


def column_major_address(base_address, i, j, n, size):
    return base_address + (i * n + j) * size


def row_major_address(base_address, i, j, m, size):
    return base_address + (i + j * m) * size


def main():
    # A 2D array is generated randomly of random size
    array = np.random.randint(10, 100, size=(random.randint(1, 10), random.randint(1, 10)))
    # Create a memory map
    filename = os_path.join(mkdtemp(), 'memorymap_array.dat')
    # w+: Create or overwrite the file, and open it for reading and writing
    memorymap_array = np.memmap(filename, dtype='int64', mode='w+', shape=array.shape)
    # This return an array with only 0s
    print("Memory Map (before):\n", memorymap_array)
    # Now, overwrite the above array
    memorymap_array[:] = array[:]
    memorymap_array.flush()  # Ensure data is written to disk

    print("Memory Map (after):\n", memorymap_array)
    print(f"Array:\n {memorymap_array}")
    print(f"Array Shape: {memorymap_array.shape}")

    print("Address Calculations")
    base_address = int(input("Enter base address: "))
    element_size = int(input("Enter the element size: "))

    i, j = map(int, input("Enter row i, column j: ").split(","))
    # Ask for re-input if the index is not valid
    while i > memorymap_array.shape[0] or j > memorymap_array.shape[1]:
        print("Invalid Input. Please input again")
        i, j = map(int, input("Enter row i, column j: ").split(","))

    m, n = memorymap_array.shape

    # Determine the row-major address
    addr_col_major = column_major_address(base_address, i, j, m, element_size)
    addr_row_major = row_major_address(base_address, i, j, n, element_size)
    print(f"+ Element array[{i}][{j}] = {memorymap_array[i][j]}")
    print(f"+ Column-major address: {addr_col_major}")
    print(f"+ Row-major address: {addr_row_major}")


main()
