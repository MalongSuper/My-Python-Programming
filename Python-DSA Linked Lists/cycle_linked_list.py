# This program implements Basic Linked List
# Detect if a linked list has cycles
# This program implements Basic Linked List
# Link: https://www.geeksforgeeks.org/dsa/floyds-cycle-finding-algorithm/
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


# We check if the list contains cycle using a set
def check_cycle(head):
    visited_node = set()
    current = head  # Start at the head node
    while current:  # while current is not None
        # If the current node is already visited
        if current in visited_node:
            return True  # There is a cycle
        visited_node.add(current)
        # Move on to the next element
        current = current.next
    return False


def floyd_cycle_algorithm(head):
    # Define two nodes slow and fast
    slow = head
    fast = head
    # * The idea of the algorithm is that while traversing the list
    # * slow pointer will move one step at a time.
    # * fast pointer moves two steps at a time.
    # * If there's a cycle, the fast pointer will
    # eventually catch up with the slow pointer within the cycle because it's moving faster.
    # * If there's no cycle, the fast pointer will reach the end of the list
    # (i.e., it will become NULL).
    while fast and fast.next:  # While we have not yet reach the node with None
        # Use both fast is and fast.next to prevent any of them being None
        # E.g., if fast = None, then fast.next = None.next -> will crash
        # Since the fast node will reach the end faster than slow
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


''' Example:
A(1) → B(2) → C(3) → D(2) → None
slow = A; fast = A
while fast and fast.next:
fast = A; fast.next = B
First iteration:
    slow = slow.next        # slow = B
    fast = fast.next.next  # fast = C
    => slow → B(2); fast → C(3)
Evaluate:
while fast and fast.next:
    fast = C 
    fast.next = D 
    → Enter loop
Second iteration:
    slow = slow.next        # slow = C
    fast = fast.next.next  # fast = None
    => slow → C(3); fast → None
Evaluate:
    while fast and fast.next:
    fast = None => Condition is already False
    -> Stop the loop
'''


def main():
    print("Basic Linked List")
    linked_list = LinkedList()
    num_node = int(input("Enter number of nodes: "))
    # Head Node
    head = Node(random.randint(1, 20))
    linked_list.head = head
    current = head

    for n in range(num_node - 1):  # Create new node after node
        new_node = Node(random.randint(1, 20))
        current.next = new_node
        new_node.prev = current
        current = new_node

    # Perform the operations
    # Traverse the linked list
    print("Traverse:", end=" ")
    linked_list.traverse()
    # Check for cycle
    print("Cycle:", check_cycle(head))
    print("Cycle using Floyd:", floyd_cycle_algorithm(head))


main()
