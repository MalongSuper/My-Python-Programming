# Write a program to evaluate an expression
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


def evaluate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    else:
        return number1 / number2


def evaluate_postfix(postfix_list):  # Evaluate Postfix
    stack = Stack()
    operators = ["+", "-", "*", "/"]
    for entry in postfix_list:
        # If the formula requires two numbers
        if entry in operators:
            # Take two numbers from the stack to calculate
            b = stack.pop()
            a = stack.pop()
            # Compute and add the result to stack
            # while removing the already used numbers
            temp = evaluate(a, b, entry)
            stack.push(temp)
        else:  # If it is a number, add it to stack
            stack.push(int(entry))
    return stack.get_top()


def main():
    print("Evaluate Expression")
    try:
        postfix = input("Postfix = ")
        result = evaluate_postfix(postfix)
        print("Result =", result)
    except TypeError:
        print("Error: Invalid Data")


main()
