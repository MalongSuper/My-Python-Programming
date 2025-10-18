# This program implements a linear Queue
# Using arrays
import random


class Queue:
    def __init__(self):  # Initial queue
        self.items = []

    def is_empty(self):  # Check for empty queue
        return self.items == []

    def traverse(self):  # Traverse a queue
        if self.items:
            for item in self.items:
                print(item, end=" ")
            print()  # New line after traversing
        else:
            print("Queue is empty")

    def enqueue(self, item):  # Enqueue an item to the queue
        return self.items.insert(len(self.items), item)

    def dequeue(self):  # Dequeue an item to the queue
        return self.items.pop(0)

    def get_front(self):  # Get the front of the queue
        return self.items[0]

    def get_rear(self):  # Get the rear of the queue
        return self.items[len(self.items) - 1]

    def get_size(self):  # Size of the queue
        return len(self.items)


def main():
    queue = Queue()
    print("Linear Queue")
    number = int(input("Enter size of Queue: "))
    print("Traverse:")
    for num in range(number):
        queue.enqueue(random.randint(1, 50))
    queue.traverse()
    print("Enqueue:")
    queue.enqueue(random.randint(1, 50))
    queue.traverse()
    print("Dequeue:")
    queue.dequeue()
    queue.traverse()
    print("Get front:", queue.get_front())
    print("Get rear:", queue.get_rear())
    print("Size:", queue.get_size())


main()
