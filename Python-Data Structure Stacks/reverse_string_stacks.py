# Write a program to reverse a string using stacks
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


def reverse_string(string):
    stack = Stack()
    # Add all the strings to stack
    for char in string:
        stack.push(char)
    temp = ""
    # Take string from stack
    while not stack.is_empty():
        temp += stack.pop()  # Pop the stack to reverse it
    return temp


def main():
    print("Reversing a String")
    s = str(input("Enter a string: "))
    reversed_string = reverse_string(s)
    print("Reversed String:", reversed_string)


main()
