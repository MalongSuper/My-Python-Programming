# Red-Black Tree with Python
# Reference: https://www.programiz.com/dsa/red-black-tree 


class Node:
    def __init__(self, data, color=1): # color: 0 for red, 1 for black
        self.data = data
        self.color = color  
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, 0)  # Sentinel node, color red
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
    
    def pre_order_traversal(self, node):
        if node != self.TNULL:
            print(node.data, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
        
    def in_order_traversal(self, node):
        if node != self.TNULL:
            self.in_order_traversal(node.left)
            print(node.data, end=' ')
            self.in_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node != self.TNULL:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=' ')
    
    def search_tree(self, node, key):
        if node == self.TNULL or key == node.data:
            return node
        if key < node.data:
            self.search_tree(node.left, key)
        return self.search_tree(node.right, key)
    
    def insert_node(self, data):  # Node Insertion
        node = Node(data)
        node.parent = None
        node.data = data
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 0  # New node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 1
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def delete_node(self, data):
        node = self.root
        z = self.TNULL
        while node != self.TNULL:
            if node.data == data:
                z = node

            if node.data <= data:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.get_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 1:
            self.fix_delete(x)


    def rb_transplant(self, u, v):
        # This function replaces the subtree rooted at node u with the subtree rooted at node v
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def fix_insert(self, k): # Fix the tree after insertion
        while k.parent.color == 0:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 0:  # case 3.1
                    u.color = 1
                    k.parent.color = 1
                    k.parent.parent.color = 0
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 1
                    k.parent.parent.color = 0
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 0:  # mirror case 3.1
                    u.color = 1
                    k.parent.color = 1
                    k.parent.parent.color = 0
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:  # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 1
                    k.parent.parent.color = 0
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 1 # root is always black



    def fix_delete(self, x): # Fix the tree after deletion
        while x != self.root and x.color == 1:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 0:
                    s.color = 1
                    x.parent.color = 0
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 1 and s.right.color == 1:
                    s.color = 0
                    x = x.parent
                else:
                    if s.right.color == 1:
                        s.left.color = 1
                        s.color = 0
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 1
                    s.right.color = 1
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 0:
                    s.color = 1
                    x.parent.color = 0
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 1 and s.left.color == 1:
                    s.color = 0
                    x = x.parent
                else:
                    if s.left.color == 1:
                        s.right.color = 1
                        s.color = 0
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 1
                    s.left.color = 1
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 1 

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def get_root(self):
        return self.root
    
    def get_maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node
    
    def get_minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def get_predecessor(self, node):
        if node.left != self.TNULL:
            return self.get_maximum(node.left)
        
        y = node.parent
        while y != None and node == y.left:
            node = y
            y = y.parent
        return y
    
    def get_successor(self, node):
        if node.right != self.TNULL:
            return self.get_minimum(node.right)
        
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y


def main():
    rbt = RedBlackTree()
    rbt.insert_node(100)
    rbt.insert_node(60)
    rbt.insert_node(145)
    rbt.insert_node(21)
    rbt.insert_node(76)
    rbt.insert_node(110)
    # Traversals
    print("Pre-order Traversal:")
    rbt.pre_order_traversal(rbt.get_root())
    print("\nIn-order Traversal:")
    rbt.in_order_traversal(rbt.get_root())
    print("\nPost-order Traversal:")
    rbt.post_order_traversal(rbt.get_root())
    # Insert 32
    print("\n\nAfter inserting 32:")
    rbt.insert_node(32)
    print("Pre-order Traversal:")
    rbt.pre_order_traversal(rbt.get_root())
    print("\nIn-order Traversal:")
    rbt.in_order_traversal(rbt.get_root())
    print("\nPost-order Traversal:")
    rbt.post_order_traversal(rbt.get_root())
    # Delete 76
    print("\n\nAfter deleting 76:")
    rbt.delete_node(76)
    print("Pre-order Traversal:")
    rbt.pre_order_traversal(rbt.get_root())
    print("\nIn-order Traversal:")
    rbt.in_order_traversal(rbt.get_root())
    print("\nPost-order Traversal:")
    rbt.post_order_traversal(rbt.get_root())
    print()


main()