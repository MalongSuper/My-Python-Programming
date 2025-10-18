# This program implements linked list
# Finding the element of the linked list
# Using Recursive and Iterative approach
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        # Empty list
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" => ")
                temp = temp.next
            print("None")

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


# Check whether the key is presented in the linked list using Recursion
def search_recursive(head, key, position=0):   # Initialize the position
    if head is None:
        return False
    if head.data == key:
        return position
    # Recur for the remaining list
    return search_recursive(head.next, key, position + 1)


# Check whether the key is presented in the linked list using Iteration
def search_iterative(head, key):
    current = head
    position = 0
    # Iterate over all the nodes
    while current is not None:
        # If the current node is equal to key
        if current.data == key:
            return position
        # Move to the next node
        current = current.next
        position += 1  # Increment position
    # The node is not found
    return False


def main():
    print("Find elements in Linked List")
    linked_list = LinkedList()
    num_nodes = int(input("Enter number of nodes: "))
    for n in range(num_nodes):
        node = random.randint(0, 100)
        linked_list.insert(node)
    linked_list.traverse()
    # Input the key and search for it
    key = int(input("Enter the key: "))
    pos_recursion = search_recursive(linked_list.head, key, position=0)
    pos_iteration = search_iterative(linked_list.head, key)
    # Display the result
    if pos_recursion and pos_iteration:
        print(f"(Recursion) The element found at index {pos_recursion}")
        print(f"(Iteration) The element found at index {pos_iteration}")
    else:
        print("The element is not found")


main()
