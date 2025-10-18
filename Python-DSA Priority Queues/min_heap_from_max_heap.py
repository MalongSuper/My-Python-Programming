# Write a program to form a min tree from a max tree
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

    def min_heapify(self, pos):  # Heapify Min Heap
        if not self.is_leaf(pos):
            # In Min Heap, the child node is higher or equal to the father node
            if ((self.heap[pos] > self.heap[self.left_child(pos)])
                    or (self.right_child(pos) <= self.last
                        and self.heap[pos] > self.heap[self.right_child(pos)])):
                # Heapify the right node and recursive right child tree
                if (self.right_child(pos) <= self.last
                        and self.heap[self.right_child(pos)] < self.heap[self.left_child(pos)]):
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
                else:  # Heapify the left node
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

    def delete(self):
        size = self.last + 1
        if size <= 0:
            print("Empty Heap")
            return None
        self.heap[self.peak] = self.heap[self.last]
        self.last -= 1
        self.max_heapify(self.peak)

    def convert_min_heap(self):
        last_node = (self.last - 1) // 2
        # Range from last node to the last index, down to -1
        for i in range(last_node, -1, -1):
            self.min_heapify(i)


def main():
    print("Create Heap")
    heap = MaxHeap()
    number = int(input("Enter number of values: "))
    print("Max Heap:", end=" ")
    for num in range(number):
        values = random.randint(1, 100)
        heap.insert(values)
    heap.display()
    heap.convert_min_heap()
    print("Min Heap:", end=" ")
    heap.display()


main()
