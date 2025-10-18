# Write a program to extract the middle element using stacks
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

    def get_middle(self):  # Get the middle element in the stack
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) // 2]


def main():
    stack = Stack()
    print("Extract Middle Element (Stack)")
    # Generate a stack
    number = random.randint(5, 10)
    for i in range(number):
        stack.push(random.randint(1, 100))
    stack.display()
    # Find and display the middle element
    middle_element = stack.get_middle()
    print("The middle element in the stack:", middle_element)


main()
