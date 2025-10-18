# Duck Typing + Inheritance with Python
# Class Hello Person

# Declaring a base class that defines the generic behavior
class Person:
    greeting = ''
    intro = ''

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def say(self, message):
        print('{}: {}'.format(self.name, message))

    def sayHello(self, another):
        # greeting & intro are class attributes
        # type(self).greeting = Person.greeting
        message = '{} {}. {} {}'.format(type(self).greeting, another.name,
                                      type(self).intro, self.name)
        # Get the person who says the line
        self.say(message)


# Declaring subclasses for duck typing
class English(Person):
    greeting = 'Hello'
    intro = 'My name is'


class Vietnamese(Person):
    greeting = 'Xin Chao'
    intro = 'Toi la'


# An independent class with similar attributes to Person
''' class Dog: 
    greeting = 'Goo Goo'
    intro = 'Hzz Hzz'

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name '''
# Error: Missing required behaviors


def main():
    john = English('John')
    binh = Vietnamese('Binh')
    john.sayHello(binh)
    binh.sayHello(john)


main()
