# Login Class using Dynamic Binding
# With id() function
# Abstract Method to Customer and Admin
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def userId(self):
        return NotImplemented


class Customer(User):
    @property
    def userId(self):
        # This generates an ID for the object and stores them
        # in that memory
        return "C" + str(id(self.name))


class Administrator(User):
    @property
    def userId(self):
        # This generates an ID for the object and stores them
        # in that memory
        return "A" + str(id(self.name))


def main():
    user1 = Customer("John")
    user2 = Administrator("James")
    print(f"{user1.name}, Id: {user1.userId}")
    print(f"{user2.name}, Id: {user2.userId}")


main()
