# Write a program to convert a given decimal number to its hexadecimal equivalent
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


def decimal_to_hexadecimal(num):  # Function to convert decimal to hexadecimal
    stack = Stack()

    hexa_value = "0123456789ABCDEF"

    while num > 0:
        hexadecimal = num % 16
        # Push the binary to the stack
        stack.push(hexa_value[hexadecimal])
        num = num // 16

    # Remove the stack form and return the decimal as string
    hexadecimal_number = ""
    while not stack.is_empty():
        hexadecimal_number += str(stack.pop())
    return hexadecimal_number


def main():
    print("Decimal to Hexadecimal (Stack)")
    number = int(input("Enter a decimal number: "))
    result = decimal_to_hexadecimal(number)
    print(f"The Hexadecimal is: {result}")


main()
