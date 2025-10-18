# Median using two heaps (max-heap and min-heap)


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
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def min_heapify(self, pos):  # Heapify Min Heap
        if not self.is_leaf(pos):
            if ((self.heap[pos] > self.heap[self.left_child(pos)])
                    or (self.right_child(pos) <= self.last
                        and self.heap[pos] > self.heap[self.right_child(pos)])):
                if (self.right_child(pos) <= self.last
                        and self.heap[self.right_child(pos)] < self.heap[self.left_child(pos)]):
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
                else:
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
        for i in range(last_node, -1, -1):
            self.min_heapify(i)


class MinHeap:
    def __init__(self, maxsize=100):
        self.maxsize = maxsize
        self.heap = [0] * self.maxsize
        self.last = -1

    def insert(self, value):
        self.last += 1
        self.heap[self.last] = value
        current = self.last
        while current > 0 and self.heap[current] < self.heap[(current - 1) // 2]:
            self.heap[current], self.heap[(current - 1) // 2] = self.heap[(current - 1) // 2], self.heap[current]
            current = (current - 1) // 2

    def get_peak(self):
        return self.heap[0] if self.last >= 0 else None

    def delete(self):
        if self.last == -1:
            return None
        if self.last == 0:
            self.last -= 1
            return self.heap[0]
        root = self.heap[0]
        self.heap[0] = self.heap[self.last]
        self.last -= 1
        self.min_heapify(0)
        return root

    def min_heapify(self, pos):
        left = 2 * pos + 1
        right = 2 * pos + 2
        smallest = pos
        if left <= self.last and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right <= self.last and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != pos:
            self.heap[pos], self.heap[smallest] = self.heap[smallest], self.heap[pos]
            self.min_heapify(smallest)


def FindMedian(arr):
    max_heap = MaxHeap()  # the lower half (max-heap)
    min_heap = MinHeap()  # the upper half (min-heap)
    for num in arr:
        if max_heap.last == -1 or num < max_heap.get_peak():
            max_heap.insert(num)
        else:
            min_heap.insert(num)
        # Re-balance the heaps if their sizes differ by more than 1
        if max_heap.last > min_heap.last + 1:
            min_heap.insert(max_heap.get_peak())
            max_heap.delete()
        elif min_heap.last > max_heap.last + 1:
            max_heap.insert(min_heap.get_peak())
            min_heap.delete()
        # Calculate and print the median
        if max_heap.last > min_heap.last:
            print("Median:", max_heap.get_peak())
        elif max_heap.last < min_heap.last:
            print("Median:", min_heap.get_peak())
        else:
            print("Median:", (max_heap.get_peak() + min_heap.get_peak()) / 2)


def main():
    print("Median using two heaps")
    arr = []
    n = int(input("Enter length of array: "))
    for i in range(n):
        e = float(input(f"Enter element {i + 1}: "))
        arr.append(e)
    # Display the result
    FindMedian(arr)


main()
