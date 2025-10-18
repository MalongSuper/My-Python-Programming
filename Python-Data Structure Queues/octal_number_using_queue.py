# This program generates n-bit octal numbers using a queue

class Queue:
    def __init__(self):  # Initial queue
        self.items = []

    def is_empty(self):  # Check for empty queue
        return self.items == []

    def traverse(self):  # Traverse a queue
        count = 0
        # Modify this function to display the numbers in table
        for item in self.items:
            print("{:<5}".format(item), end=" ")
            count += 1
            if count % 10 == 0:  # 10 numbers each row
                print()
        if count % 10 != 0:
            print()

    def enqueue(self, item):  # Enqueue an item to the queue
        return self.items.insert(len(self.items), item)

    def dequeue(self):  # Dequeue an item to the queue
        return self.items.pop(0)

    def size(self):  # Size of the queue
        return len(self.items)


def main():
    queue = Queue()
    print("Octal number with Queue")
    number = int(input("Enter number of bits: "))
    print(f"Generate {number}-bit octal numbers: ")
    for num in range(1, 2 ** number):
        octal_number = oct(num)[2:]  # Use oct() function
        queue.enqueue(octal_number)
    queue.traverse()


main()
