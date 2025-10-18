# Login Class using Dynamic Binding

class User:
    __userid = 0

    def __init__(self, name):
        self.__name = name
        User.__userid += 1
        self.__sid = User.__userid

    @property
    def name(self):
        return self.__name

    @property
    def userId(self):
        return self.__sid


def main():
    user1 = User("John")
    user2 = User("Adam")
    print(f"{user1.name}, Id: {user1.userId}")
    print(f"{user2.name}, Id: {user2.userId}")


main()
