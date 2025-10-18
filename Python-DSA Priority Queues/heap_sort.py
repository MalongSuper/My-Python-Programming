# Write a program to implement heap sort
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


def heap_sort(array):  # This function performs heap sort using array
    heap = MaxHeap(len(array))  # Max size is the number of elements of the heap
    # It will be converted to array
    for num in array:
        heap.insert(num)  # Insert the value to the array

    sorted_array = []
    while heap.last >= 0:  # The loop ends when there is no more value in heap
        max_value = heap.heap[heap.peak]  # Take the top node in the heap
        sorted_array.append(max_value)  # Append it to the array
        heap.delete()  # Delete the value
        # The heapify begins to ensure father node is better than child node
        # Thus, the highest value is always in the top node
    return sorted_array[::-1]


def main():
    print("Heap Sort")
    heap = MaxHeap()
    heap_array = []
    number = int(input("Enter number of values: "))
    print("Heap:", end=" ")
    for num in range(number):
        values = random.randint(1, 100)
        heap.insert(values)
    heap.display()
    # Sort the heap
    for h in range(heap.last + 1):  # Iterate all the values in heap
        heap_array.append(heap.heap[h])
    # Heap Sort
    sorted_heap = heap_sort(heap_array)
    print("Sorted Heap:", end=" ")
    for sort_heap in sorted_heap:
        print(sort_heap, end=" ")


main()
