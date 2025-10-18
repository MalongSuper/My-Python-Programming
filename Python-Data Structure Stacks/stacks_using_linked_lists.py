# Write a program to implement stacks using linked lists
import numpy as np
import random


class Node:
    def __init__(self, data):
        self.data = data  # Point at a target data
        self.next = None

    def display(self):
        print(self.data, '->', end=' ')


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None  # Keep track of the end of the stack

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        while current is not None:
            current.display()
            current = current.next
        print()

    def push(self, data):
        new_node = Node(data)
        if self.top is None:  # Stack is empty
            self.top = new_node
            self.tail = new_node
        else:  # Insert at the end
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None  # Return None if the stack is empty

        if self.top == self.tail:  # Only one element
            data = self.top
            self.top = None
            self.tail = None
            return data

        # More than one element: traverse to find the second last node
        current = self.top
        while current.next != self.tail:
            current = current.next

        data = self.tail
        self.tail = current  # Update tail to the second last node
        self.tail.next = None  # Remove the last node
        return data

    def get_top(self):
        if self.is_empty():
            return None
        return self.tail.data  # Return the last added item


def main():
    print("Linked List to Stack")
    stack = Stack()
    size = int(input("Enter size of linked list: "))
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
