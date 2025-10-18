# Write a program to merge two heaps
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

    def merge_heap(self, heap_two):
        # Indicate merge heap that will combine two heaps
        merged_heap = MaxHeap(self.maxsize + heap_two.maxsize)
        # Insert element from the heap one
        for i1 in range(self.last + 1):
            merged_heap.insert(self.heap[i1])
        # Insert element from the heap two
        for i2 in range(heap_two.last + 1):
            merged_heap.insert(heap_two.heap[i2])
        # Heapify the merged heap
        for i in range(merged_heap.last, -1, -1):
            merged_heap.max_heapify(i)
        # Update the current heap with the merge heap
        self.heap = merged_heap.heap
        self.last = merged_heap.last
        return self  # Return the merged heap


def main():
    print("Create Heap")
    heap1 = MaxHeap()
    heap2 = MaxHeap()
    number1 = int(input("Enter number of values in Heap 1: "))
    number2 = int(input("Enter number of values in Heap 2: "))
    # Display Heap 1
    print("Heap 1:", end=" ")
    for num1 in range(number1):
        values = random.randint(1, 100)
        heap1.insert(values)
    heap1.display()
    # Display Heap 2
    print("Heap 2:", end=" ")
    for num2 in range(number2):
        values = random.randint(1, 100)
        heap2.insert(values)
    heap2.display()
    # Merge Heap1 with heap 2
    print("Merged Heap:", end=" ")
    heap1.merge_heap(heap2)
    heap1.display()


main()
