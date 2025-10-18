# This program creates a non-recursive Merge Sort using stacks.
import numpy as np


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # Check if a stack is empty
        return len(self.items) == 0

    def display(self):  # Traverse all nodes
        for i in range(len(self.items)):
            print(self.items[i], "->", end=" ")
        print()

    def push(self, data):  # Append a value to the stack
        self.items.append(data)

    def pop(self):  # Take the top value out of the stack
        if self.is_empty():  # Empty stack
            return None
        else:
            return self.items.pop()

    def get_top(self):  # Get a value at the top of the stack
        if self.is_empty():
            return None
        else:
            return self.items[-1]


def merge(arr1, arr2):  # Function to merge two sub arrays
    merged = []
    i, j = 0, 0
    # Merge two arrays in ascended order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Append remaining element of two arrays
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


def merge_sort(arr):  # Function to merge sort array
    stack = Stack()
    # Push element in array onto the stack as a sub array
    for element in arr:
        stack.push([element])
    # Merge adjacent sub-arrays until only one sub-array remains
    while len(stack.items) > 1:
        first = stack.pop()
        second = stack.pop()
        merged = merge(first, second)
        stack.push(merged)

    # The remaining item on the stack is the sorted array
    return stack.pop()


def main():
    print("Non-recursive Merge Sort (Stack)")
    size = int(input("Enter size of array: "))
    array = np.random.randint(1, 100, size=size)
    print("Original Array:", array)
    sorted_array = merge_sort(array)
    print("Sorted Array:", np.array(sorted_array))


main()
