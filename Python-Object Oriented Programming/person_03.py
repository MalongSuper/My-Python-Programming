# Class Meeting using Duck Typing

class Person:  # The first class Person
    greeting = ''
    bye = ''
    intro = ''
    song = ''

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def say(self, message):  # Get the person who says the line
        print(f"{self.name}: {message}")

    def say_hello(self, another):
        message = f"{self.greeting} {another.name}. {self.intro} {self.name}"
        self.say(message)

    def say_goodbye(self, another):
        message = f"{self.bye}. {another.name}"
        self.say(message)

    def sing(self):
        self.say(self.song)


# Duck Typing with inheritance
class English(Person):
    greeting = 'Hello'
    bye = 'Good bye'
    intro = 'My name is'
    song = 'Happy birthday to you...'


class Spanish(Person):
    greeting = 'Hola'
    bye = 'Adios'
    intro = 'Me llamo'
    song = 'Cumpleanos felliz'


# Duck Typing is in this class, say_hello(), say_goodbye(), song()
# are used in add_member(), remove_member(), and song()
# The class does not care about whether the member is English or Spanish,
# if the methods in Person are called, they are Person
class Meeting:
    def __init__(self, head):  # Take the name of the head member
        self._head = head
        self._members = [head]
        # Initially, this person is added to the member list

    def add_member(self, member):
        # Append this person to the list
        self._members.append(member)
        self._head.say_hello(member)
        member.say(f"{member.greeting} {self._head.name}")

    def remove_member(self, member):
        if member == self._head:
            raise ValueError('You cannot remove the head from the meeting')
        # Remove this person to the list
        self._members.remove(member)
        member.say_goodbye(self._head)

    def song(self):
        for member in self._members:
            member.sing()


def main():
    peter = English('Peter')
    john = English('John')
    martinez = Spanish('Martinez')
    meeting = Meeting(peter)
    meeting.add_member(john)
    meeting.add_member(martinez)
    meeting.remove_member(john)
    meeting.song()


main()
