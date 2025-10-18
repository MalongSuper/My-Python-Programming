# Abstract Class Animal
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def greets(self):  # Abstract method,
        # since there is no implementation
        return NotImplemented

    def __str__(self):  # Concrete method
        return "This is an animal"


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    # Use the abstract method
    def greets(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    # Use the abstract method
    def greets(self):
        print("Woof")

    @staticmethod
    def greets_dog(another_dog):
        # Use is_instance to check if another_dog is a Dog
        if isinstance(another_dog, Dog):
            print("Woooof")
        else:
            print("None")


class BigDog(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def greets(self):
        print("Wooow")

    @staticmethod
    def greets_dog(another_dog):
        if isinstance(another_dog, BigDog):
            print("Wooooooooow")
        elif isinstance(another_dog, Dog):
            print("Woooooow")
        else:
            print("None")


def main():
    cat1 = Cat("Jim")
    dog1 = Dog("Pat")
    cat2 = Cat("James")
    dog2 = Dog("Peter")
    bigdog1 = BigDog("Bill")
    bigdog2 = BigDog("White")
    cat1.greets()
    dog2.greets()
    cat2.greets()
    dog1.greets_dog(dog2)
    dog1.greets_dog(cat2)
    bigdog1.greets()
    bigdog2.greets()
    bigdog1.greets_dog(bigdog2)
    bigdog1.greets_dog(dog1)
    bigdog1.greets_dog(dog2)
    bigdog1.greets_dog(cat2)


main()
