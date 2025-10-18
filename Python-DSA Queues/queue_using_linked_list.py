# Queue using linked lists
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):  # Initial queue
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):  # Check for empty queue
        return self.size == 0

    def traverse(self):  # Traverse a queue
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  # New line after traversing

    def enqueue(self, item):  # Enqueue an item to the queue
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):  # Dequeue an item to the queue
        if self.is_empty():
            print("Queue is empty")
        removed_data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return removed_data

    def get_front(self):  # Get the front of the queue
        if self.is_empty():
            print("Queue is empty")
        return self.front.data

    def get_rear(self):  # Get the rear of the queue
        if self.is_empty():
            print("Queue is empty")
        return self.rear.data

    def get_size(self):  # Size of the queue
        return self.size


def main():
    queue = Queue()
    print("Queue (Linked Lists)")
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
