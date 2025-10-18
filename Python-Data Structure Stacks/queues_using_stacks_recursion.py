# Write a program to implement a Queue using a stack
# Using different method Recursion
import random
import time


class Queue:
    def __init__(self):
        self.stack = []  # The different method only requires one stack

    def enqueue(self, x):  # Enqueue item from a queue
        # Base case
        while len(self.stack) == 0:
            self.stack.append(x)
            return

        # Recursive
        item = self.stack.pop()
        self.enqueue(x)
        self.stack.append(item)

    def dequeue(self):  # Enqueue item from a queue
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def display_queue(self):
        if len(self.stack) == 0:
            print("Queue is empty")
        else:
            for element in self.stack[::-1]:  # Reversing self stack
                print(element, end=" ")


def main():
    print("Queue using a stack (Recursion)")
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
    time.sleep(5)
    print("\nResult:\nThe recursive method is simpler, "
          "while the previous method is more efficient for general operation")
    print("The decision of which one is better "
          "might be based on the performance of the system")


main()
