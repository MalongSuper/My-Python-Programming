# # This program implements Chaining in Hashing
import numpy as np
# Initialize N
number = 100


# Define a node for linked list in chaining
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def hash_function(key):
    return key % number


def separate_chaining(key, hash_table):  # Define insert chaining function
    index = hash_function(key)
    if hash_table[index] is None:
        hash_table[index] = Node(key)
    else:
        current = hash_table[index]
        while current.next is not None:
            current = current.next
        current.next = Node(key)


def count_collisions(hash_table):  # Count collisions for chaining
    collisions = 0
    for slot in hash_table:
        if slot is not None:
            count = 0
            current = slot
            while current is not None:
                count += 1
                current = current.next
            if count > 1:
                collisions += (count - 1)
    return collisions


def display(hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] is None:  # Empty Hash Table
            print(f"Hash Table[{i}]: None")
        else:
            print(f"Hash Table[{i}]: ", end="")
            current = hash_table[i]
            while current is not None:
                print(current.key, end=" --> ")
                current = current.next
            print("None")


def main():
    print("Hashing (Separate Chaining)")
    # Create an array of 100 random numbers
    keys = np.random.randint(1, 1000, 100)
    # Initialize Hash Table as a list of None value
    hash_table = [None] * number
    # Insert key to hash table using chaining
    for key in keys:
        separate_chaining(key, hash_table)
    # Display Hash Table
    display(hash_table)
    # Convert misses list to array
    collision = count_collisions(hash_table)
    print("=================================")
    print("Number of Collisions:", collision)
    print("=================================")


main()
