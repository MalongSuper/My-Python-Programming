# This program implements AVL Tree

class CircularQueue:
    def __init__(self, maximum=100):
        self.maximum = maximum
        self.front = -1
        self.rear = -1
        self.items = [None] * maximum

    def is_empty(self):
        return self.front == -1

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
        return True

    def dequeue(self):  # Dequeue the element to the queue
        if self.front != -1:
            temp = self.items[self.front]
            self.remove()
            return temp
        else:
            print("Queue is empty")
            return False

    def traverse(self):
        front_index = self.front  # Front index
        rear_index = self.rear  # Rear index
        if front_index == -1:  # Front is the last index
            print("Queue is empty")
            return
        if front_index <= rear_index:
            while front_index <= rear_index:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
        else:
            # From the beginning to last index
            while front_index <= self.maximum - 1:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
            # Take the remaining item of the queue to the beginning of the list
            front_index = 0  # Back to the beginning of the list
            while front_index <= rear_index:
                print(f"{self.items[front_index]} <-", end=" ")
                front_index += 1
        print()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left node
        self.right = None  # Right node
        self.height = 1  # Height of the tree

    def __str__(self):
        return f"[{self.data}]"

    def display(self):
        if self.data is not None:
            print(f"{self.data} [h={self.height}]", end=", ")


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def process_node(node):  # Process through the node to display
        if node is not None:
            node.display()

    def traverse(self):
        self.breadth_first_traverse(self.root)

    def breadth_first_traverse(self, root_node):  # Bread-First Traversal
        # Without recursion, we use circular queue to order the nodes
        current = root_node
        if current is None:
            print("Tree is empty")
            return
        nodes_queue = CircularQueue()  # Implements Circular Queue
        nodes_queue.enqueue(current)

        while not nodes_queue.is_empty():
            # Dequeue the node and execute it
            node = nodes_queue.dequeue()
            self.process_node(node)
            # When taking a current node to a queue to execute
            # Enqueue its children (left and right) to the queue for the next execution
            if node.left is not None:
                nodes_queue.enqueue(node.left)
            if node.right is not None:
                nodes_queue.enqueue(node.right)

    @staticmethod
    def get_height(current):  # Height of AVL Tree
        if current is None:
            return 0
        return current.height

    def get_balance_factor(self, current):  # Balance factor of AVL Tree
        if current is None:
            return 0
        return self.get_height(current.left) - self.get_height(current.right)

    def insert(self, data):  # Insert the AVL tree
        self.root = self.insert_tree(self.root, data)

    def insert_tree(self, current, data):
        if current is None:
            return Node(data)
        if data < current.data:
            # Recursively call the left node
            current.left = self.insert_tree(current.left, data)
        elif data > current.data:
            # Recursively call the right node
            current.right = self.insert_tree(current.right, data)
        else:  # If node is already full
            print("Node exists:", data)
            return current
        # Update the height of child trees with current node
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        # Update the balance factor and re-balance the tree
        balance = self.get_balance_factor(current)
        if balance > 1:  # Root balance is better than 1, the tree is inclined to the left
            # New node will be on the left side of the left node
            if data < current.left.data:
                return self.right_rotate(current)
            else:  # Rotate Left-Right
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)
        if balance < -1:  # Root balance is less than -1, the tree is inclined to the right
            # New node will be on the right side of the right node
            if data > current.right.data:
                return self.left_rotate(current)
            else:
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)

        return current

    def find_min(self, root):  # Find the minimum element of the tree (leftmost node)
        if root.left is None:  # If there is no left node, return the data
            return root.data
        else:
            return self.find_min(root.left)  # Recursively move to the left

    def delete(self, data):
        self.root = self.delete_tree(self.root, data)

    def delete_tree(self, current, data):  # Delete a node in the tree
        if current is None:
            print(f"Node {data} not found")
            return
        if data < current.data:  # Deleted node is at the left
            # Recursively call the left node
            current.left = self.delete_tree(current.left, data)
        elif data > current.data:  # Deleted node is at the right
            # Recursively call the right node
            current.right = self.delete_tree(current.right, data)
        else:  # Current is the deleted node
            if current.left is None:  # There is only right branch
                temp = current.right
                return temp
            elif current.right is None:  # There is only left branch
                temp = current.left
                return temp
            # Replace the deleted node by the leftmost node of the right child
            temp = self.find_min(current.right)
            current.data = temp
            # The replaced node should be deleted in its original position
            current.right = self.delete_tree(current.right, temp)
    # Update the height and the balance factor
        balance = self.get_balance_factor(current)
        if balance > 1:  # Tree is inclined on the left
            if self.get_balance_factor(current.left) >= 0:  # Left child
                return self.right_rotate(current)
            else:  # Right child
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)
        if balance < -1:  # Tree is inclined on the right
            if self.get_balance_factor(current.right) <= 0:  # Right child
                return self.left_rotate(current)
            else:  # Left child
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)

        return current

    def left_rotate(self, x):  # Left rotate the node to re-balance tree
        y = x.right  # Node y is in right side of x, y becomes root node
        beta = y.left  # Call beta on the left side of y
        y.left = x  # The left side of y becomes x
        x.right = beta  # The right side of x becomes beta
        # Compute the height of x before y since x is below y
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):  # Right rotate the node to re-balance tree
        x = y.left  # Node x is in left side of y, x becomes root node
        beta = x.right  # Call beta on the right side of x
        x.right = y  # The right side of x becomes y
        y.left = beta  # The left side of y becomes beta
        # Compute the height of y before x since y is below x
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x


def main():
    print("Create AVL Tree")
    avl_tree = AVLTree()
    nodes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for nod in nodes:
        avl_tree.insert(nod)
    avl_tree.traverse()
    # Insert numbers
    insert_numbers = [2048, 4096, 1, 8192]
    for num in insert_numbers:
        print(f"\nInsert {num}: ")
        avl_tree.insert(num)
        avl_tree.traverse()
    # Delete numbers
    deleted_numbers = [8, 512, 4096, 1]
    for num in deleted_numbers:
        print(f"\nDelete {num}: ")
        avl_tree.delete(num)
        avl_tree.traverse()


main()
