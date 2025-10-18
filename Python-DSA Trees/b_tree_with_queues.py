# Implement B-Tree using Circular Queues


class CircularQueue:
    def __init__(self, maximum=100):  # Add maximum length
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


# Implement B-Tree
t = 3  # t: min number of child nodes in each node, exclude root
max_keys = 2 * t - 1  # 2t - 1: Max keys in each node
max_children = 2 * t  # 2t: max number of child nodes, exclude root


class BNode:
    def __init__(self, leaf=False):
        self.is_leaf = leaf
        self.keys = []
        self.child = []

    def display(self):
        print("|", self.keys, "|")

    # Operation of one node
    def insert_non_full(self, key):
        i = len(self.keys) - 1  # Current number of keys
        if self.is_leaf:  # If it is leaf node, simple
            # Add 1 key and re-order the keys (right shift)
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:  # Finding the child nodes to add
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1  # Since child[i] points to the child nodes contains elements < keys[i]
            if len(self.child[i].keys) == max_keys:  # If child nodes have full number of keys
                self.split_child(self.child[i], i)
                if key > self.keys[i]:
                    i += 1
            self.child[i].insert_non_full(key)  # Add to the child node

    # Split keys in node x, self is the parent node of x
    def split_child(self, x, i):
        median = int(max_keys / 2)  # Median key
        z = BNode(x.is_leaf)  # Create new nodes at the right to split
        self.child.insert(i + 1, z)  # Pointer at the new node at the right
        self.keys.insert(i, x.keys[median])  # Take the median key up to the parent node
        z.keys = x.keys[median + 1: max_keys]  # Keys of the new right node
        x.keys = x.keys[0: median]  # Keys of the new left node
        if not x.is_leaf:  # Update pointer to the child nodes
            z.child = x.child[median + 1: max_keys]
            x.child = x.child[0: median + 1]


class BTree:
    def __init__(self):
        self.root = BNode(leaf=True)

    def search(self, key):
        self.search_tree(key, self.root)

    # current: node with BNode style
    def search_tree(self, key, current=None):
        if current is not None:
            n = len(current.keys)
            i = 0
            while i < n and key > current.keys[i]:
                i += 1
            if i < n and key == current.keys[i]:
                return current, i  # Found the position i of the current node
            elif current.is_leaf:
                return None  # Not found
            else:  # Found below the child node
                return self.search_tree(key, current.child[i])
        else:
            return None

    def insert(self, key):
        current = self.root
        # If the root is full -> Add the new node (temp) as root
        # and temp.child[0] points at the old root node
        # split the old root node to 2 nodes by adding node z to the right
        # re-divide the key and the child nodes pointers
        # Finally, insert key to the new root node (temp)
        if len(current.keys) == max_keys:  # Split the root node
            temp = BNode()
            self.root = temp
            temp.child.insert(0, current)  # temp.child[0] = current
            temp.split_child(temp.child[0], 0)
            temp.insert_non_full(key)
        else:
            # If the node is not full (spaces left) -> If the root is leaf, then add node and re-order
            # Else -> Recursively call to insert to the corresponding leaf
            current.insert_non_full(key)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.child:
                self.print_tree(child, level + 1)

    def traverse(self):
        current = self.root
        if current is None:
            print("Empty Tree")
            return
        # Apply Circular Queue
        nodes_queue = CircularQueue()
        nodes_queue.enqueue(current)
        while not nodes_queue.is_empty():
            # Remove the node out of the queue and execute it
            node = nodes_queue.dequeue()
            node.display()
            # Note that when removing a current node out of the queue to execute
            # Have to move the child nodes (left, right) to the queue
            # So that we can execute them later
            for child in node.child:
                nodes_queue.enqueue(child)


def main():
    btree = BTree()
    print("t =", t)
    keys = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    for k in keys:
        btree.insert(k)
    btree.print_tree(btree.root)
    btree.traverse()


main()
