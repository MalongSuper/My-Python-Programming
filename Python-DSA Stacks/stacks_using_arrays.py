# Write a program to implement stacks using arrays
import numpy as np
import random


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


def main():
    print("Array to Stack")
    stack = Stack()
    size = int(input("Enter size of array: "))
    array = np.random.randint(1, 10, size=size)
    for arr in array:
        stack.push(arr)  # Add each random value
    print("Stack Display:", end=" ")
    stack.display()
    print("Stack Push:", end=" ")
    stack.push(random.randint(1, 10))
    stack.display()
    print("Stack Pop:", end=" ")
    stack.pop()
    stack.display()
    print("Stack Get Top:", end=" ")
    print(stack.get_top())


main()
