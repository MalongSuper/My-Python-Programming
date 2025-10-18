# This program generates all possible trees from given values

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left node
        self.right = None  # Right node


def generate_tree(numbers):  # Generate tree
    if not numbers:  # Base Case: Tree is empty
        return [None]

    trees = []
    # Iterate through all values from the list
    for i, num in enumerate(numbers):
        left_subtrees = generate_tree(numbers[:i])
        right_subtrees = generate_tree(numbers[i+1:])
        # Looping and connecting all the left and right subtrees with current node
        for left in left_subtrees:
            for right in right_subtrees:
                node = Node(num)  # Making node value as root
                node.left = left  # Connect left subtree
                node.right = right  # Connect right subtree
                trees.append(node)  # Add the tree to the list
    return trees


def traverse_trees(node):  # Traverse all the trees
    if node:
        print(node.data, end=" ")  # Data of the current node
        traverse_trees(node.left)
        traverse_trees(node.right)


print("Generate all possible trees using given values")
nodes = [10, 67, 24, 76, 90, 56, 223, 89, 113, 91]
all_trees = generate_tree(nodes)
for index, tree in enumerate(all_trees):
    print(f"Tree {index + 1}: ", end="")
    traverse_trees(tree)
    print()
