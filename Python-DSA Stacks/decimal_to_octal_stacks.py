# Write a program to convert a given decimal number to its octal equivalent
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


def decimal_to_octal(num):  # Function to convert decimal to octal
    stack = Stack()

    while num > 0:
        octal = num % 8
        # Push the binary to the stack
        stack.push(octal)
        num = num // 8

    # Remove the stack form and return the octal as string
    octal_number = ""
    while not stack.is_empty():
        octal_number += str(stack.pop())
    return octal_number


def main():
    print("Decimal to Octal (Stack)")
    number = int(input("Enter a decimal number: "))
    result = decimal_to_octal(number)
    print(f"The Octal is: {result}")


main()
