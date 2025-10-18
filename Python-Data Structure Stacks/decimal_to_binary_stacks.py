# Write a program to convert a given decimal number to its binary equivalent
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


def decimal_to_binary(num):  # Function to convert decimal to binary
    stack = Stack()

    while num > 0:
        binary = num % 2
        # Push the binary to the stack
        stack.push(binary)
        num = num // 2

    # Convert the elements in stack form to return the binary as string
    binary_number = ""
    while not stack.is_empty():
        binary_number += str(stack.pop())
    return binary_number


def main():
    print("Decimal to Binary (Stack)")
    number = int(input("Enter a decimal number: "))
    result = decimal_to_binary(number)
    print(f"The Binary is: {result}")


main()
