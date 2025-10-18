# This program implements B-Tree Sequence 1

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


def main():
    print("Create B-Tree (Sequence 1)")
    t = 3
    b_tree = BTree(t)
    key_nodes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for node in key_nodes:
        # Traverse the tree at every step
        print(f"Insert {node}: ")
        b_tree.insert(node)
        b_tree.traverse(b_tree.root)


main()
