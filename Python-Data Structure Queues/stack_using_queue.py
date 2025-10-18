# This program implements Stack using one Queue
import random


class Queue:
    def __init__(self):  # Initial queue
        self.items = []

    def is_empty(self):  # Check for empty queue
        return self.items == []

    def traverse(self):  # Traverse a queue
        for item in self.items:
            print(item, end=" ")

    def enqueue(self, item):  # Enqueue an item to the queue
        return self.items.insert(len(self.items), item)

    def dequeue(self):  # Dequeue an item to the queue
        return self.items.pop(0)

    def size(self):  # Size of the queue
        return len(self.items)


class Stack:
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):  # Check if a stack is empty
        return self.queue.is_empty()

    def display(self):  # Traverse all nodes
        self.queue.traverse()

    def push(self, item):  # Append a value to the stack
        self.queue.enqueue(item)

    def pop(self):  # Take the top value out of the stack
        if not self.is_empty():
            size = self.queue.size()
            for _ in range(size - 1):
                dequeued_item = self.queue.dequeue()
                self.queue.enqueue(dequeued_item)
            # Dequeue the last item which is top of the stack
            return self.queue.dequeue()
        else:
            print("Stack is empty!!")

    def get_top(self):  # Get a value at the top of the stack
        if self.is_empty():
            return None
        else:
            return self.queue.items[-1]


def main():
    stack = Stack()
    print("Stack using single Queue")
    size = int(input("Enter size of Stack: "))
    for s in range(size):
        stack.push(random.randint(1, 100))
    stack.display()
    print("\nPush:")
    stack.push(random.randint(1, 100))
    stack.display()
    print("\nPop:")
    stack.pop()
    stack.display()
    print("\nGet Top:")
    print(stack.get_top())


main()
