# This program implements Binary Search Tree
# Use Recursion, Depth-first Traversal
import random


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

    def traverse(self, order=None):
        if order == "in-order":
            self.inorder_traverse(self.root)
        elif order == "post-order":
            self.postorder_traverse(self.root)
        elif order == "pre-order":
            self.preorder_traverse(self.root)
        else:
            # Display in In-Order as Default
            self.inorder_traverse(self.root)

    def inorder_traverse(self, root_node):  # Function to display tree in In-order
        # In order: Left => Root => Right
        if root_node is None:
            return
        self.inorder_traverse(root_node.left)
        self.process_node(root_node)
        self.inorder_traverse(root_node.right)

    def postorder_traverse(self, root_node):  # Function to display tree in Post-order
        # Post order: Left => Right => Root
        if root_node is None:
            return
        self.postorder_traverse(root_node.left)
        self.postorder_traverse(root_node.right)
        self.process_node(root_node)

    def preorder_traverse(self, root_node):  # Function to display tree in Pre-order
        # Pre order: Root => Left => Right
        if root_node is None:
            return
        self.process_node(root_node)
        self.preorder_traverse(root_node.left)
        self.preorder_traverse(root_node.right)

    def search(self, data):
        return self.search_tree(self.root, data)

    def search_tree(self, current, data):  # Find the value and display the index
        if current is None:
            print(f"Node {data} not found")
            return False
        if data == current.data:
            print(f"Node {data} found")
            return True
        if data < current.data:  # If the data is lower than the current root
            # Proceed to the left
            return self.search_tree(current.left, data)
        else:
            # Else, proceed to the left
            return self.search_tree(current.right, data)

    def find_max(self):  # Find the maximum value in Tree (Rightmost)
        if self.root is None:
            print("Tree is empty")
            return None

        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def find_min(self):  # Find the minimum value in Tree (Leftmost)
        if self.root is None:
            print("Tree is empty")
            return None

        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

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
            return
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

    def merge(self, tree_two):
        if tree_two.root is None:
            print("Tree Two is empty")
            return
        self.merge_trees(self.root, tree_two.root)

    def merge_trees(self, current_tree, current_tree_two):  # Merge two Trees
        if current_tree_two is not None:
            # Append the data of Tree Two
            self.insert(current_tree_two.data)
            # Merge the trees in left and right nodes
            self.merge_trees(current_tree, current_tree_two.left)
            self.merge_trees(current_tree, current_tree_two.right)

    def find_predecessor(self, data):  # Find predecessor of a given node
        predecessor = None
        current = self.root

        while current is not None:
            if data == current.data:  # If the data is equal to current node
                # The max value is the predecessor in the left subtree
                if current.left is not None:
                    predecessor = current.left
                    while predecessor.right is not None:
                        predecessor = predecessor.right
                break
            elif data < current.data:  # If the data is lower than current node
                # Proceed to the next left subtree
                current = current.left
            else:  # Else, the data is greater than current node
                # Update the predecessor, then proceed to the next left subtree
                predecessor = current
                current = current.right

        # Display the predecessor
        if predecessor is not None:
            print(f"Predecessor of {data} is {predecessor.data}")
        else:
            print(f"Predecessor of {data} not found")


def main():
    print("Binary Search Tree")
    array1 = [10, 67, 24, 76, 90, 56, 223, 89, 113, 91]
    array2 = [11, 68, 26, 78, 95, 58, 225, 99, 110, 87]
    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()
    for a in array1:
        bst1.insert(a)
    for b in array2:
        bst2.insert(b)
    bst1.traverse(order='in-order')
    print()
    bst1.traverse(order='post-order')
    print()
    bst1.traverse(order='pre-order')
    print()
    bst1.search(90)
    print("Max:", bst1.find_max())
    print("Min:", bst1.find_min())
    bst1.insert(8)
    bst1.insert(2)
    bst1.insert(78)
    bst1.traverse(order='in-order')
    print()
    bst1.delete(20)
    bst1.delete(10)
    bst1.delete(56)
    bst1.traverse(order='in-order')
    print()
    bst1.merge(bst2)
    bst1.traverse(order='in-order')


main()
