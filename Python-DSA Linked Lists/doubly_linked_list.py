# This program implements Doubly Linked List
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        # Empty list
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <=> ")
                temp = temp.next
            print("None")

    def search(self, data):
        # Search the value and return its position
        temp = self.head
        position = 1
        while temp:
            if temp.data == data:
                return position
            temp = temp.next
            position += 1
        return -1

    def get_size(self):
        # Return length of the linked list
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_certain_position(self, data, position):
        if position < 1:
            print("Position is invalid")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            for i in range(position - 2):
                if temp is None:
                    print("Position is invalid")
                    return
                temp = temp.next
            if temp is None or temp.next is None:  # Insert at the end
                self.insert_end(data)
            else:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_certain_position(self, position):
        if position < 1:
            print("Position is invalid")
            return
        if self.head is None:
            print("List is empty")
            return
        if position == 1:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        for i in range(position - 2):
            if temp is None or temp.next is None:
                print("Position is invalid")
                return
            temp = temp.next
        if temp.next is None:
            print("Position is invalid")
            return
        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp


def main():
    print("Doubly Linked List")
    doubly_linked_list = DoublyLinkedList()
    num_nodes = int(input("Enter number of nodes: "))
    for n in range(num_nodes):
        node = random.randint(0, 100)
        doubly_linked_list.insert_begin(node)
    # Traverse
    print("Traverse: ")
    doubly_linked_list.traverse()
    # Insert node at the beginning
    insert_node_beg = random.randint(0, 100)
    print(f"Insert {insert_node_beg} at the beginning: ")
    doubly_linked_list.insert_begin(insert_node_beg)
    doubly_linked_list.traverse()
    # Insert node at the end
    insert_node_end = random.randint(0, 100)
    print(f"Insert {insert_node_end} at the end: ")
    doubly_linked_list.insert_end(insert_node_end)
    doubly_linked_list.traverse()
    # Insert node at the certain position
    insert_node_pos = random.randint(0, 100)
    pos_beg = random.randint(1, doubly_linked_list.get_size())
    print(f"Insert {insert_node_pos} at position {pos_beg}: ")
    doubly_linked_list.insert_certain_position(insert_node_pos, pos_beg)
    doubly_linked_list.traverse()
    # Delete node at the beginning
    print("Delete at the beginning: ")
    doubly_linked_list.delete_begin()
    doubly_linked_list.traverse()
    # Delete node at the end
    print("Delete at the end: ")
    doubly_linked_list.delete_end()
    doubly_linked_list.traverse()
    # Delete node at the end
    pos_end = random.randint(1, doubly_linked_list.get_size())
    print(f"Delete at the position {pos_end}: ")
    doubly_linked_list.delete_certain_position(pos_end)
    doubly_linked_list.traverse()


main()
