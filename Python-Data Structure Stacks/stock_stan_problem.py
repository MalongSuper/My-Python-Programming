# Write a program to solve Stock Stan Problem
# Then find the span of a stock in a day
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


def calculate_span(price, s):
    # Create a stack and push an index of first element
    stack = Stack()
    stack.push(0)
    n = len(price)
    # Span value of first element is always 1
    s[0] = 1
    # Calculate span for rest of the elements
    for i in range(1, n):
        # While stack is not empty and the top of the stack is lower than price of i
        while not stack.is_empty() and price[stack.get_top()] <= price[i]:
            stack.pop()
        # If stack becomes empty, price[i] is greater
        s[i] = i + 1 if stack.is_empty() else (i - stack.get_top())
        stack.push(i)


def main():
    # Find the span of a stock in a day
    print("Stock Span Problem")
    day = 7
    price = np.random.randint(10, 100, size=day)
    spans = [0] * day  # Array to store the spans
    calculate_span(price, spans)
    print("Your Daily Price:", price)
    print("Spans:", np.array(spans))


main()
