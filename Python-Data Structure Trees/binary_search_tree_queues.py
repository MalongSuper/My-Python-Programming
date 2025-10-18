# This program implements Binary Search Tree
# Use Queues, Breadth-first Traversal
import random


class CircularQueue:
    def __init__(self, maximum=100):  # Add maximum length
        self.maximum = maximum
        self.front = -1
        self.rear = -1
        self.items = [None] * maximum
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def remove(self):
        # Check for empty list
        if self.front == -1:  # Last element in the list
            return False
        # Only one item in the queue
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Front is the last item in the list (last index)
            if self.front == self.maximum - 1:
                self.front = 0
            else:
                self.front += 1
        return True

    def enqueue(self, data):  # Enqueue the element to the queue
        if (self.front == 0 and self.rear == self.maximum - 1) or (self.front == self.rear + 1):
            print("Queue Overflow")
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            if self.rear == self.maximum - 1:
                self.rear = 0
            else:
                self.rear += 1
        self.items[self.rear] = data
        self.size += 1
        return True

    def dequeue(self):  # Dequeue the element to the queue
        if self.front != -1:
            temp = self.items[self.front]
            self.remove()
            self.size -= 1
            return temp
        else:
            print("Queue is empty")
            return False


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left node
        self.right = None  # Right node

    def display(self):  # Display Tree
        if self.data is not None:
            print(self.data, end="  ")


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.level = 0

    @staticmethod
    def process_node(node):  # Process through the node to display
        if node is not None:
            node.display()

    def traverse(self):
        self._breadth_first_traverse(self.root)

    def insert(self, data):
        self.root = self.insert_tree(self.root, data)

    # current: current node / sub-tree root node
    def insert_tree(self, current, data):  # Insert node to tree
        if current is None:
            return Node(data)
        if data < current.data:  # Call the left side if data < current data
            current.left = self.insert_tree(current.left, data)
        elif data > current.data:  # Call the right side if data > current data
            current.right = self.insert_tree(current.right, data)
        else:  # Node is already exists:
            print(f"Node {data} already exists")
            return current
        return current

    def _breadth_first_traverse(self, root_node):
        current = root_node
        if current is None:
            print("Empty tree")
            return
        nodes_queue = CircularQueue()
        nodes_queue.enqueue(current)
        while not nodes_queue.is_empty():
            # Take the node out of the queue and execute this node
            node = nodes_queue.dequeue()
            self.process_node(node)
            # Note that when taking a current_node out of the queue to analyze
            # We have to put the child nodes (left, right) to the queue
            # For next execution
            if node.left is not None:
                nodes_queue.enqueue(node.left)
            if node.right is not None:
                nodes_queue.enqueue(node.right)


def main():
    bst = BinarySearchTree()
    bst.traverse()
    n = int(input("Enter size of the tree: "))
    for i in range(n):
        bst.insert(random.randint(1, 300))
    bst.traverse()
    bst.insert(random.randint(1, 300))
    print("\nInsertion:")
    bst.traverse()
    print()
    bst.insert(random.randint(1, 300))
    bst.traverse()


main()
