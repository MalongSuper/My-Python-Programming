# Linked List using Stack
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):  # Check if the stack is empty
        return self.top is None

    def display(self):  # Traversing all nodes
        current = self.top
        if self.is_empty():
            print("Stack is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next

    def push(self, item):  # Add element onto the stack
        # In linked list, it is insertion at the end
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
        else:
            current = self.top
            while current.next:
                current = current.next
            current.next = new_node

    def pop(self):  # Remove element onto the stack
        # In linked list, it is deletion at the end
        if self.is_empty():
            print("Stack is empty")
            return None
        if self.top.next is None:  # Only one element
            popped_node = self.top
            self.top = None
            return popped_node.data

        # More than one element
        current = self.top
        while current.next and current.next.next:
            current = current.next

        popped_node = current.next
        current.next = None
        return popped_node.data

    def get_top(self):  # Get the top value of the stack
        # In linked list, it is the last node
        if self.is_empty():
            print("Stack is empty")
            return None
        current = self.top
        while current.next:
            current = current.next
        return current.data


def main():
    print("Stack using Linked List")
    stack = Stack()
    num_stack = int(input("Enter number of values in Stack: "))
    # Create Stack
    for n in range(num_stack):
        stack.push(random.randint(1, 100))
    print("Display: ", end="")
    stack.display()
    print("\nIs Empty:", stack.is_empty())
    print("Push: ", end="")
    stack.push(random.randint(1, 100))
    stack.display()
    print("\nPop: ", end="")
    stack.pop()
    stack.display()
    print("\nGet top:", stack.get_top())


main()
