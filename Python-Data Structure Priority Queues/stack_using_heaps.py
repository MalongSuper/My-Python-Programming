# Implement stack using heaps.
import random


class MaxHeap:
    def __init__(self, maxsize=100):
        self.maxsize = maxsize
        self.heap = [0] * self.maxsize  # First element
        self.last = -1  # Last element in the heap
        self.peak = 0  # The element at the top position

    @staticmethod
    def parent(pos):
        return (pos - 1) // 2  # Index at father node

    @staticmethod
    def left_child(pos):  # Index at left child
        return 2 * pos + 1

    @staticmethod
    def right_child(pos):  # Index at the right child
        return 2 * pos + 2

    def is_leaf(self, pos):  # Leaf node: No left node
        return self.left_child(pos) > self.last

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, value):
        if self.last >= self.maxsize:
            print("Overflow")
            return
        self.last += 1
        self.heap[self.last] = value
        # Put the highest element to the root node
        current = self.last
        while (self.parent(current) >= 0 and
               self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def display(self):
        for i in range(self.last + 1):
            print(self.heap[i], end=" ")
        print()

    def get_peak(self):
        if self.last >= 0:
            return self.heap[self.peak]

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            # In Max Heap, the child node is smaller than the father node
            if (self.heap[pos] < self.heap[self.left_child(pos)] or
                    self.heap[pos] < self.heap[self.right_child(pos)]):
                # Heapify the left node and recursive left child tree
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:  # Heapify the right node
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def delete(self):
        size = self.last + 1
        if size <= 0:
            print("Empty Heap")
            return None
        self.heap[self.peak] = self.heap[self.last]
        self.last -= 1
        self.max_heapify(self.peak)


class Stack:
    def __init__(self):
        self.heap = MaxHeap()

    def display(self):
        self.heap.display()

    def push(self, item):
        self.heap.insert(item)

    def pop(self):
        if self.heap.last == -1:
            print("Stack is empty")
            return None
        else:
            # Change the peak value to the last value
            # To pop the last value
            self.heap.peak = self.heap.last
            self.heap.delete()


def main():
    stack = Stack()
    print("Stack using Heap")
    size = int(input("Enter size of Stack: "))
    for s in range(size):
        stack.push(random.randint(1, 100))
    stack.display()
    print("Push:")
    stack.push(random.randint(1, 100))
    stack.display()
    print("Pop:")
    stack.pop()
    stack.display()


main()
