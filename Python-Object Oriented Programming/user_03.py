# Login Class using Dynamic Binding
# With id() function

class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def userId(self):
        # This generates an ID for the object and stores them
        # in that memory
        return id(self.__name)


def main():
    user1 = User("John")
    user2 = User("Adam")
    print(f"{user1.name}, Id: {user1.userId}")
    print(f"{user2.name}, Id: {user2.userId}")


main()
