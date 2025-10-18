# Linked List using Queue 
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def traverse(self):  # Traverse
        current = self.front  # Instead of head
        while current:
            print(current.data, end="  ")
            current = current.next

    def is_empty(self):  # Check if the queue is empty
        return self.front is None

    def enqueue(self, item):  # Enqueue value to queue
        # In linked list, it is insertion at the end
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):  # Dequeue value to queue
        # In linked list, it is deletion at the beginning
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

    def get_front(self):  # Get the front value of queue
        # In linked list, it is the first node
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.front.data


def main():
    print("Queue using Linked List")
    queue = Queue()
    num_queue = int(input("Enter number of values in Queue: "))
    # Create Queue
    for n in range(num_queue):
        random_value = random.randint(1, 100)
        queue.enqueue(random_value)
    print("Traverse: ", end="")
    queue.traverse()
    print("\nIs Empty:", queue.is_empty())
    print("Enqueue: ", end="")
    queue.enqueue(random.randint(1, 100))
    queue.traverse()
    print("\nDequeue: ", end="")
    queue.dequeue()
    queue.traverse()
    print("\nGet Front:", queue.get_front())


main()
