# Write a program to extract the minimum element using stacks
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

    def get_min(self):  # Get the minimum element in the stack
        if self.is_empty():
            return None
        else:
            return min(self.items)


def main():
    stack = Stack()
    print("Extract Minimum Element (Stack)")
    # Generate a stack
    number = random.randint(5, 10)
    for i in range(number):
        stack.push(random.randint(1, 100))
    stack.display()
    # Find and display the minimum element
    min_element = stack.get_min()
    print("The minimum element in the stack:", min_element)


main()
