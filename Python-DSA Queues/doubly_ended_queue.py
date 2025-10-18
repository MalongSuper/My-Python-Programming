# This program implements a Doubly-Ended Queue (Deque)
import random


class Node:  # Create a node to represent node in doubly linked list
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.datas = []

    def is_empty(self):  # Check for empty queue
        return self.size == 0

    def enqueue_front(self, data):  # Enqueue an element at the front end
        new_node = Node(data)  # Create a new node
        if self.is_empty():  # If the node is empty
            self.front = self.rear = new_node
        else:  # Proceed to the next node as front
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1  # Increase the size after adding an element

    def enqueue_rear(self, data):  # Enqueue an element at the rear end
        new_node = Node(data)  # Create a new node
        if self.is_empty():  # If the node is empty
            self.front = self.rear = new_node
        else:  # Proceed to the prev node as rear
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1  # Increase the size after adding an element

    def dequeue_front(self):  # Dequeue at the front end
        if self.is_empty():
            print("Deque is empty")
            return None
        removed_data = self.front.data  # Remove the front data
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            # Proceed to the next front
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1  # Decrease the size after removing an element
        return removed_data

    def dequeue_rear(self):  # Dequeue at the rear end
        if self.is_empty():
            print("Deque is empty")
            return None
        removed_data = self.rear.data  # Remove the rear data
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            # Proceed to the previous rear
            self.rear = self.rear.prev
            self.rear.next = None  # When it is none, the data is removed
        self.size -= 1  # Decrease the size after removing an element
        return removed_data

    def traverse(self):  # Traverse a Deque
        if self.is_empty():
            print("Deque is empty")
            return
        current = self.front
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        print("None")


def main():
    deque = Deque()
    print("Doubly-ended Queue (Deque)")
    number = int(input("Enter the size of Deque: "))
    for num in range(number):
        deque.enqueue_front(random.randint(1, 100))
    print("Traverse:")
    deque.traverse()
    print("Enqueue Front:")
    deque.enqueue_front(random.randint(1, 100))
    deque.traverse()
    print("Enqueue Rear:")
    deque.enqueue_rear(random.randint(1, 100))
    deque.traverse()
    print("Dequeue Front:")
    deque.dequeue_front()
    deque.traverse()
    print("Dequeue Rear:")
    deque.dequeue_rear()
    deque.traverse()


main()
