# Hospital Management using Heap


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

    # We need to adjust max_heapify() to ensure that tuples
    # are compared using the priority number only.
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


def determine_priority(age):  # Priority order for hospital management
    # 1 – Toddlers (3 to 5 years old);
    if 3 <= age <= 5:
        return 1
    # 2 – Teen (6 to 10 years old);
    elif 6 <= age <= 10:
        return 2
    # 3 – Elders (60 years old or above);
    elif 60 <= age:
        return 3
    # 4 – Adolescents (11 to 18 years old);
    elif 11 <= age <= 18:
        return 4
    # 5 – Normal patients (all the remaining ages).
    else:
        return 5


def hospital_management():
    print("Hospital Management using Heap")
    heap = MaxHeap()
    queue = []
    patient = []
    number = int(input("Enter the number of patient: "))
    # Input patient name and age
    for n in range(number):
        print(f"Patient {n + 1}")
        patient_name = str(input("Enter Patient name: "))
        patient_age = int(input("Enter Patient age: "))
        patient.append((patient_name, patient_age))
    # Create a tuple of patient and their priority
    for name, age in patient:
        priority = determine_priority(age)
        heap.insert((name, priority))
    # Display the order of serving
    while heap.last >= 0:
        queue.append(heap.get_peak())  # Append it to queue
        heap.delete()
    # Sort the queue based on the priority order
    print("Order of serving based on priority")
    for patient, priority in sorted(queue, key=lambda x: x[1]):
        print(f"+ Name: {patient}, Priority: {priority}")


# Run the main code
hospital_management()
