# Basic Hashing - Hash Tables
from hash_code_hashing import hash_code
import numpy as np


def hash_function(key, c):  # Find the hash function by modulo
    n = len(key)
    hash_func = []
    for j in range(n):  # Find the hash code
        hash_value = hash_code(key[j])
        hash_func.append(hash_value)
    hash_index = {}
    for k in range(len(hash_func)):  # Find the index of the value
        index = hash_func[k] % c  # Calculate the modulo
        hash_index[hash_func[k]] = index  # Append it to the dictionary
    return hash_index


def hash_table(index):
    print(index)
    # Set an initial dictionary using the maximum values
    hash_table = {i: [] for i in range(max(index.values()) + 1)}
    for i in index:  # Iterate through the dictionary
        hash_table[index[i]].append(i)  # Append it to the list
    return hash_table


def main():
    print("Hashing - Hash Table")
    n = int(input("Enter number of values: "))
    key = []
    # Input strings
    for i in range(n):
        string = str(input(f"Enter string {i + 1}: "))
        key.append(string)
    # Hash Function --> Hash Table
    hash_func = hash_function(key, 10)
    table = hash_table(hash_func)
    # Display the result
    print(f"\nHash Table")
    for i in table:
        print(f"{i}: {table[i]}")


if __name__ == "__main__":
    main()
