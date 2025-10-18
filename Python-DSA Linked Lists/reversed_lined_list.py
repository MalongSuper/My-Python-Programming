# This program implements linked list
# Reverse, concatenate linked list
# Check if the linked list contains a cycle
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

    def reverse(self):  # Reverse the linked list
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next  # Keep the node after current
            current.next = previous
            previous = current  # Move two pointers to one element
            current = next_node
        self.head = previous

    def copy(self):  # Copy list
        temp = LinkedList()
        current = self.head()
        while current is not None:
            temp.insert(current.data)
            current = current.next
        return temp

    def concatenate(self, another):  # Concatenate two lists
        list1 = self.copy()
        list2 = another.copy()
        # Using operator overriding
        current = list1.head
        while current.next:
            current = current.next
        current.next = list2.head
        return list1

    def check_cycle(self): # Check if the list contains cycle
        nodes = set()
        current = self.head
        while True:
            if (current is None) or (current in nodes):
                break
            nodes.add(current)
            current = current.next
        # The iteration ends when returning back to the first node
        # Or None is encountered
        if current is None:
            return False
        else:
            return True


def main():
    print("Reverse Linked List")
    linked_list = LinkedList()
    num_nodes = int(input("Enter number of nodes: "))
    for n in range(num_nodes):
        node = random.randint(0, 100)
        linked_list.insert(node)
    linked_list.traverse()
    # Reverse the list
    linked_list.reverse()
    print("Reverse:")
    linked_list.traverse()


main()
