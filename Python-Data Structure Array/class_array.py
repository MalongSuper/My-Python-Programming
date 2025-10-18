# Array using Class Module with basic functions
import random


class Array:
    def __init__(self, maximum):
        self.maximum = maximum
        self.n = 0
        self.arr = [0] * maximum  # Use list to simulate array

    def traverse(self):
        print(self.arr[:self.n])

    def insert_begin(self, item):
        if self.n < self.maximum:  # n increases/decreases by 1
            for i in range(self.n, 0, -1):
                self.arr[i] = self.arr[i - 1]

            self.arr[0] = item
            self.n += 1  # Increase the length of the array
        else:
            print("Overflow")

    def insert_end(self, item):
        if self.n < self.maximum:
            self.arr[self.n] = item
            self.n += 1  # Increase the length of the array
        else:
            print("Overflow")

    def insert_position(self, item, pos):
        if self.n < self.maximum:
            if 0 <= pos <= self.n:
                for i in range(self.n, pos, -1):
                    self.arr[i] = self.arr[i - 1]
                self.arr[pos] = item
                self.n += 1
            else:
                print("Out of bound")
        else:
            print("Overflow")

    def delete_begin(self):
        if self.n > 0:
            for i in range(self.n - 1):
                self.arr[i] = self.arr[i + 1]
            self.arr[self.n - 1] = 0
            self.n -= 1
        else:
            print("Underflow")

    def delete_end(self):
        if self.n > 0:
            self.n -= 1
            self.arr[self.n] = 0  # Clear the last element
        else:
            print("Underflow")

    def delete_position(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.arr[i] = self.arr[i + 1]
            self.arr[self.n - 1] = 0  # Clear the last element
            self.n -= 1
        else:
            print("Underflow")

    def find_element(self, item):
        for i in range(self.n):
            if self.arr[i] == item:
                return i  # Return the index of found element
        return -1


def main():
    print("Array (using Class)")
    array = Array(100)
    n = int(input("Enter size of the array: "))
    for i in range(n):
        array.insert_begin(random.randint(1, 100))
    print("Array:")
    array.traverse()
    # Insert at the beginning
    print("Insert at the beginning:")
    array.insert_begin(random.randint(1, 100))
    array.traverse()
    # Insert at the end
    print("Insert at the end:")
    array.insert_end(random.randint(1, 100))
    array.traverse()
    # Insert a certain position
    pos_begin = random.randint(0, n - 1)
    print("Insert at position", pos_begin, "\b:")
    array.insert_position(random.randint(1, 100), pos_begin)
    array.traverse()
    # Delete at the beginning
    print("Delete at the beginning:")
    array.delete_begin()
    array.traverse()
    # Delete at the beginning
    print("Delete at the end:")
    array.delete_end()
    array.traverse()
    # Delete a certain position
    pos_del = random.randint(0, n - 1)
    print("Delete at position", pos_del, "\b:")
    array.delete_position(pos_del)
    array.traverse()


main()
