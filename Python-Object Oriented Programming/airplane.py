# Duck Typing of Airplane and Bird


class Bird:
    objects = "bird"

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def fly(self):
        print(f"The {self.objects} {self.name} is flying")


class Airplane:
    objects = "airplane"

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def fly(self):
        print(f"The {self.objects} {self.name} is flying")


def main():
    bird = Bird("Pogo")
    airplane = Airplane("Jet Plane")
    bird.fly()
    airplane.fly()


main()
