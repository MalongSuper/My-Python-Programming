# Write a program to implement two stacks using a single list
import random
import time


class TwoStack:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1  # Last element of Top 1
        self.top2 = self.size  # First element of Top 2

    # Push an element x to Stack 1
    def push1(self, x):
        # If there is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")
            exit(1)

    # Push an element x to Stack 1
    def push2(self, x):
        # If there is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")
            exit(1)

    # Pop an element from the first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    # Pop an element from the second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            exit()


def display_stacks(two_stacks):  # Function to display stack
    print("Stack 1:")
    for s1 in range(two_stacks.top1 + 1):
        print(two_stacks.arr[s1], end=" -> ")
    print()

    print("Stack 2:")
    for s2 in range(two_stacks.size - 1, two_stacks.top2 - 1, -1):
        print(two_stacks.arr[s2], end=" -> ")
    print()


def main():
    print("Two Stacks using single list")
    two_stack = TwoStack(random.randint(1, 20))
    number = int(input("Enter the size of two stacks: "))
    # Display stack with push value
    for i in range(number):
        two_stack.push1(random.randint(1, 20))
        two_stack.push2(random.randint(1, 20))
    print("Display Stacks")
    display_stacks(two_stack)
    time.sleep(3)

    # Display stack with pop value
    print("Pop Element from Stacks")
    two_stack.pop1()
    two_stack.pop2()
    display_stacks(two_stack)
    time.sleep(3)

    # Display stack with new push value
    print("Push Element from Stacks")
    two_stack.push1(random.randint(1, 20))
    two_stack.push2(random.randint(1, 20))
    display_stacks(two_stack)
    time.sleep(3)


main()
