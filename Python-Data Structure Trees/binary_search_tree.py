# This program implements Binary Search Tree
import time
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left node
        self.right = None  # Right node

    def display(self):  # Display Tree
        if self.data is not None:
            print(self.data, end="  ")


def process_node(node):  # Process through the node to display
    if node is not None:
        node.display()


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.level = 0

    def traverse(self):
        self.inorder_traverse(self.root)

    def inorder_traverse(self, root_node):  # Display tree in in-order
        # In order: Left => Root => Right
        if root_node is None:
            return
        self.inorder_traverse(root_node.left)
        process_node(root_node)
        self.inorder_traverse(root_node.right)

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

        # Find leftmost value to replace after deletion
    def find_min_tree(self, root):  # Root: any root in the tree
        if root.left is None:  # No left root, return data
            return root.data
        else:
            return self.find_min_tree(root.left)

    def delete(self, data):
        self.root = self.delete_tree(self.root, data)

    def delete_tree(self, current, data):  # Delete data in Tree
        if current is None:
            print(f"Node {data} not found")
        if data == current.data:
            # Three cases for delete data
            # Case 1: Delete Node without left or right node connected to it
            if (current.left is None) and (current.right is None):
                return None
            # Case 2: Delete Node has one left node or right node
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            # Case 3: Delete Node has both left and right nodes => Find the leftmost
            min_right = self.find_min_tree(current.right)
            current.data = min_right
            # After replacing, the leftmost value of right subtree must be deleted
            current.right = self.delete_tree(current.right, min_right)
            return current
        # If not, proceed to the next left or right value
        if data < current.data:
            current.left = self.delete_tree(current.left, data)
            return current
        else:
            current.right = self.delete_tree(current.right, data)
            return current


def main():
    binary_search_tree = BinarySearchTree()
    nodes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    # Create a Binary Search Tree
    print("Create Binary Search Tree")
    for node in nodes:
        binary_search_tree.insert(node)
    binary_search_tree.traverse()
    # Delete a random element
    print("\nDelete element")
    random_value = random.choice(nodes)
    # Calculate average time
    start = time.time()
    binary_search_tree.delete(random_value)
    binary_search_tree.traverse()
    end = time.time()
    print(f"\nElement {random_value} deleted")
    print(f"Average Time: {end - start}")


main()
