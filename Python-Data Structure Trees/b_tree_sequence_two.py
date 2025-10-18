# This program implements B-Tree Sequence 2

class Node:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):  # "t" represents the minimum degree of B-Tree
        self.root = Node(True)
        self.t = t

    def traverse(self, x, level=0):  # Traverse the B-Tree
        print(f"Level {level}: ", end="")
        for i in x.keys:
            print(i, end=" ")
        print()
        level += 1
        if len(x.child) > 0:
            for i in x.child:
                self.traverse(i, level)

    def insert(self, k):  # "k" refers to key values
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node(False)
            self.root = temp  # Root node becomes temp
            temp.child.insert(0, root)  # Add it to children
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)  # Create space for the new key
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(leaf=y.leaf)
        x.keys.insert(i, y.keys[t - 1])
        x.child.insert(i + 1, z)
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def delete(self, k):  # Delete a node
        return self.delete_recursive(self.root, k)

    def delete_recursive(self, x, k):  # Delete node using recursion
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:  # Key found in current node
            if x.leaf:  # Key found in leaf node
                del x.keys[i]
            else:  # Key found in internal node
                y = x.child[i]
                z = x.child[i + 1]

                if len(y.keys) >= self.t:  # Case 1: y has enough keys
                    x.keys[i] = self.delete_predecessor(y)
                elif len(z.keys) >= self.t:  # Case 2: z has enough keys
                    x.keys[i] = self.delete_successor(z)
                else:  # Case 3: Merge y and z
                    self.merge_nodes(x, i)

        else:  # Key not found in current node
            if x.leaf:
                print(f"Key {k} not found")
                return
            else:
                if len(x.child[i].keys) < self.t:
                    self.fill_child(x, i)
                if i > len(x.keys):
                    # Recursive call the function
                    self.delete_recursive(x.child[i - 1], k)
                else:
                    self.delete_recursive(x.child[i], k)

    def merge_nodes(self, x, i):  # Merge node
        y = x.child[i]
        z = x.child[i + 1]
        y.keys.append(x.keys[i])
        y.keys.extend(z.keys)
        y.child.extend(z.child)
        del x.keys[i]
        del x.child[i + 1]

        if x == self.root and not x.keys:
            self.root = y

    def fill_child(self, x, i):
        if i != 0 and len(x.child[i - 1].keys) >= self.t:
            self.borrow_from_prev(x, i)
        elif i != len(x.keys) and len(x.child[i + 1].keys) >= self.t:
            self.borrow_from_next(x, i)
        elif i != len(x.keys):
            self.merge_nodes(x, i)
        else:
            self.merge_nodes(x, i - 1)

    def delete_predecessor(self, x):
        if x.leaf:
            return x.keys.pop()
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self.t:
            self.delete_recursive(x.child[n], x.keys[n])
        else:
            self.fill_child(x, n)
            self.delete_recursive(x.child[n], x.keys[n])

    def delete_successor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.t:
            self.delete_recursive(x.child[0], x.keys[0])
        else:
            self.fill_child(x, 0)
            self.delete_recursive(x.child[0], x.keys[0])

    @staticmethod
    def borrow_from_prev(x, i):
        child = x.child[i]
        sibling = x.child[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        if not child.leaf:
            child.child.insert(0, sibling.children.pop())
        x.keys[i - 1] = sibling.keys.pop()

    @staticmethod
    def borrow_from_next(x, i):
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        if not child.leaf:
            child.child.append(sibling.children.pop(0))
        x.keys[i] = sibling.keys.pop(0)


def main():
    print("Create B-Tree (Sequence 2)")
    t = 3
    b_tree = BTree(t)
    sequence = [3, 8, 1, 78, 623, 24, 90, 23, 89, 12, 7, 52, 167, 233, 190]
    for node in sequence:
        # Traverse the tree at every step
        print(f"Insert {node}")
        b_tree.insert(node)
        b_tree.traverse(b_tree.root)
    # Delete nodes
    deleted_keys = [52, 167]
    for key in deleted_keys:
        print(f"Delete {key}: ")
        b_tree.delete(key)
        b_tree.traverse(b_tree.root)


main()
