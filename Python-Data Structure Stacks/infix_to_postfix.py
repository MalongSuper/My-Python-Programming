# Write a program to convert infix to postfix
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


def get_precedence(operator):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    return precedence.get(operator, 0)


def infix_to_postfix(infix_list):
    operators = ["+", "-", "*", "/"]
    stack = Stack()
    postfix = []  # List contains all the numbers/operators in postfix
    for entry in infix_list:
        # Opening parenthesis
        if entry == "(":
            stack.push(entry)  # Add it to the stack
        # Closing parenthesis
        elif entry == ")":
            entry2 = stack.pop()  # Remove it from the stack
            while entry2 != "(":
                # Get all the numbers/operator inside the stack to the postfix
                postfix.append(entry2)
                entry2 = stack.pop()  # After that, remove the value from the stack
        # Operators
        elif entry in operators:
            if not stack.is_empty():  # Not empty stack
                precedence = get_precedence(entry)
                entry2 = stack.pop()
                # While the precedence of the current operator
                # is not better than the previous one
                while precedence <= get_precedence(entry2):
                    postfix.append(entry2)
                    if not stack.is_empty():
                        entry2 = stack.pop()
                    else:
                        break
                # Push the operator combined with the entry back to stack
                if precedence > get_precedence(entry2):
                    stack.push(entry2)
            # Put the operator back to stack
            stack.push(entry)

        else:
            # For numbers, they are default put into the postfix
            postfix.append(entry)

    # Other remaining values are added to the postfix
    while not stack.is_empty():
        postfix.append(stack.pop())

    return postfix


def main():
    print("Convert Infix to Postfix")
    infix = input("Infix = ")
    result = infix_to_postfix(infix)
    print("Postfix =", " ".join(result))


main()
