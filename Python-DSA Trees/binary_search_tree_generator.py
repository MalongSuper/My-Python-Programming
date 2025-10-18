# Binary Search Tree Generator
import tkinter as tk
import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def get_nodes(self):
        nodes = []
        self._inorder_traversal(self.root, nodes)
        return nodes

    def _inorder_traversal(self, node, nodes):
        if node:
            self._inorder_traversal(node.left, nodes)
            nodes.append(node)
            self._inorder_traversal(node.right, nodes)


class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

    def draw_tree(self, bst):
        self.canvas.delete("all")
        if bst.root:
            self._draw_node(bst.root, 400, 50, 200)

    def _draw_node(self, node, x, y, dx):
        if node:
            radius = 20
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='white', outline='black')
            self.canvas.create_text(x, y, text=str(node.value), fill='black')

            if node.left:
                new_x, new_y = x - dx, y + 100
                self.canvas.create_line(x, y + radius, new_x, new_y - radius, fill='black')
                self._draw_node(node.left, new_x, new_y, dx / 2)

            if node.right:
                new_x, new_y = x + dx, y + 100
                self.canvas.create_line(x, y + radius, new_x, new_y - radius, fill='black')
                self._draw_node(node.right, new_x, new_y, dx / 2)


class App:
    def __init__(self, root):
        self.root = root
        self.bst = BinarySearchTree()
        self.visualizer = BSTVisualizer(root)

        # Frame for input elements
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.label = tk.Label(self.input_frame, text="Enter number of nodes:")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.input_frame)
        self.entry.pack(side=tk.LEFT)

        self.generate_button = tk.Button(self.input_frame, text="Generate", command=self.generate_tree)
        self.generate_button.pack(side=tk.LEFT)

    def generate_tree(self):
        num_nodes = int(self.entry.get())
        self.bst = BinarySearchTree()
        values = random.sample(range(1, num_nodes * 2), num_nodes)
        for value in values:
            self.bst.insert(value)
        self.visualizer.draw_tree(self.bst)


def main():
    root = tk.Tk()
    root.title("Binary Search Tree Generator")
    root.resizable(False, False)
    App(root)
    root.mainloop()


main()
