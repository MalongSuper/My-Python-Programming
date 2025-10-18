# Class Animal

class Animal:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'Animal[name="{self.name}"]'


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Mammal[Animal[name="{self.name}"]]'


class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Cat[Mammal[Animal[name="{self.name}"]]'

    @staticmethod
    def greets():
        print("Meow")


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Dog[Mammal[Animal[name="{self.name}"]]'

    @staticmethod
    def greets():
        print("Woof")

    @staticmethod
    def greets_dog(another_dog):
        # Use is_instance to check if another_dog is a Dog
        if isinstance(another_dog, Dog):
            print("Woooof")
        else:
            print("None")


def TestAnimal():
    animal1 = Dog("Butter")
    animal2 = Cat("Chili")
    animal3 = Cat("Jordan")
    animal4 = Dog("Martha")
    # Printing
    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)
    # Greeting
    animal1.greets()
    animal2.greets()
    animal3.greets()
    animal4.greets()
    animal1.greets_dog(animal4)
    animal4.greets_dog(animal1)
    animal4.greets_dog(animal2)


TestAnimal()
