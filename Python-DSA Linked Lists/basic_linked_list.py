# This program implements Basic Linked List
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, value):  # Find and return node containing value
        temp = self.head
        position = 0
        while (temp.data != value) and (temp.next is not None):
            position += 1
            temp = temp.next

        if temp.data != value:  # If the node is not found
            return False

        # Display node position
        return position + 1

    def traverse(self):  # Traverse the linked list
        current = self.head
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        print("None")

    def reverse(self):  # Reverse the linked list
        current = self.head
        temp = None
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def insert(self, data):  # Insert the node based on the order of the values
        temp = Node(data)
        # Empty list
        if self.head is None:
            self.head = temp
            return
        else:
            if temp.data <= self.head.data:
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
                return

        # Other cases
        current = self.head
        while (current.next is not None) and (current.data < temp.data):
            current = current.next

        if current.next is not None:
            temp.next = current
            temp.prev = current.prev
            current.prev.next = temp
            current.prev = temp
        else:
            current.next = temp
            temp.prev = current


def main():
    print("Basic Linked List")
    linked_list = LinkedList()
    num_node = int(input("Enter number of nodes: "))
    # Head Node
    head = Node(random.randint(1, 100))
    linked_list.head = head
    current = head

    for n in range(num_node - 1):  # Create new node after node
        new_node = Node(random.randint(1, 100))
        current.next = new_node
        new_node.prev = current
        current = new_node

    # Perform the operations
    # Traverse the linked list
    print("Traverse")
    linked_list.traverse()
    # Find a value
    print("\nReturn the node containing the value")
    val = random.randint(1, 100)
    print(f"Find {val}")
    pos = linked_list.search(val)
    if pos is False:
        print("Value not found")
    else:
        print(f"Value {val} in node {pos}")
    # Reverse the linked list
    print("Reverse the linked list")
    linked_list.reverse()  # This function only reverse the list
    linked_list.traverse()
    # Insert new node based on the order of the value
    print("\nInsert new node based on the order of the value")
    value = random.randint(1, 100)
    linked_list.reverse()
    linked_list.insert(value)
    linked_list.traverse()
    print("\nNew value inserted:", value)


main()
