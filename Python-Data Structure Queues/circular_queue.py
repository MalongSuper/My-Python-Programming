# This program implements a circular Queue
import random


class CircularQueue:
    def __init__(self, maximum=100):  # Add maximum length
        self.maximum = maximum
        self.front = -1
        self.rear = -1
        self.items = [None] * maximum

    def is_empty(self):
        return self.front == -1

    def remove(self):
        # Check for empty list
        if self.front == -1:  # Last element in the list
            return False
        # Only one item in the queue
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Front is the last item in the list (last index)
            if self.front == self.maximum - 1:
                self.front = 0
            else:
                self.front += 1
        return True

    def enqueue(self, data):  # Enqueue the element to the queue
        if (self.front == 0 and self.rear == self.maximum - 1) or (self.front == self.rear + 1):
            print("Queue Overflow")
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            if self.rear == self.maximum - 1:
                self.rear = 0
            else:
                self.rear += 1
        self.items[self.rear] = data
        return True

    def dequeue(self):  # Dequeue the element to the queue
        if self.front != -1:
            temp = self.items[self.front]
            self.remove()
            return temp
        else:
            print("Queue is empty")
            return False

    def traverse(self):
        front_index = self.front  # Front index
        rear_index = self.rear  # Rear index
        if front_index == -1:  # Front is the last index
            print("Queue is empty")
            return
        if front_index <= rear_index:
            while front_index <= rear_index:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
        else:
            # From the beginning to last index
            while front_index <= self.maximum - 1:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
            # Take the remaining item of the queue to the beginning of the list
            front_index = 0  # Back to the beginning of the list
            while front_index <= rear_index:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
        print()


def main():
    circular_queue = CircularQueue()
    print("Circular Queue")
    number = int(input("Enter size of Circular Queue: "))
    print("Traverse:")
    for num in range(number):
        circular_queue.enqueue(random.randint(1, 50))
    circular_queue.traverse()
    print("Enqueue:")
    circular_queue.enqueue(random.randint(1, 50))
    circular_queue.traverse()
    print("Dequeue:")
    circular_queue.dequeue()
    circular_queue.traverse()


main()
