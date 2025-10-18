# Generate Binary Numbers using Queue
class Queue:
    def __init__(self, maximum):  # Initial queue
        self.items = []
        self.maximum = maximum

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

    def size(self):  # Size of the queue
        return len(self.items)


def binary_numbers(bits):  # n: number of bits
    n = 2 * bits
    queue = Queue(maximum=n)  # Queue with 2^n elements
    queue.enqueue("1")    # Binary numbers begin with 1
    for i in range(n - 1):
        item = queue.dequeue()
        print(item, end=", ")
        queue.enqueue(item + "0")
        queue.enqueue(item + "1")


def main():
    print("Generate binary numbers using Queue")
    n = int(input("Enter n (bits): "))
    binary_numbers(n)


main()
