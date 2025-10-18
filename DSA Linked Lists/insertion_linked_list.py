# This program implements Linked List
# Perform insertion in linked list based on increasing order of data
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" => ")
                temp = temp.next
            print("None")

    def insert(self, data):
        temp = Node(data)
        # Empty list
        if self.head is None:
            self.head = temp
            return
        else:  # Node is at the beginning of the list
            if temp.data <= self.head.data:  # Minimum value in list
                temp.next = self.head
                self.head = temp
                return
        # Other cases
        previous = self.head
        current = self.head
        while (current is not None) and (current.data < temp.data):
            # Keep the pointer of previous element
            # so that later add temp after previous
            previous = current
            current = current.next
        # temp is always between previous and current
        # or at the end of the list
        # When current = None
        temp.next = current
        previous.next = temp


def main():
    print("Linked List with order elements")
    linked_list = LinkedList()
    num_nodes = int(input("Enter number of nodes: "))
    for n in range(num_nodes):
        node = random.randint(0, 100)
        linked_list.insert(node)
    linked_list.traverse()


main()
