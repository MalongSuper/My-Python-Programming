# Write a program to implement a Queue using a stack
import random


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):  # Enqueue item from a queue
        # Move all elements from stack 1 to stack 2
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        # Push item into self stack 1
        self.stack1.append(x)

        # Push all elements back to stack 1
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):  # Enqueue item from a queue
        if len(self.stack1) == 0:
            return -1
        # Return top of self.s1
        x = self.stack1[-1]
        self.stack1.pop()
        return x

    def display_queue(self):
        if len(self.stack1) == 0:
            print("Queue is empty")
        else:
            for element in self.stack1:
                print(element, end=" ")


def main():
    print("Queue using a stack")
    queue = Queue()
    number = int(input("Enter the size of Queue: "))
    for i in range(number):
        queue.enqueue(random.randint(1, 20))

    print("Queue:", end=" ")
    queue.display_queue()
    print("\nEnqueue:", end=" ")
    queue.enqueue(random.randint(1, 20))
    queue.display_queue()
    print("\nDequeue:", end=" ")
    queue.dequeue()
    queue.display_queue()


main()
