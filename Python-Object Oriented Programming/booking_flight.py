# Class Booking Flight in Python

class AirlineCompany:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f'Airline Company: {self.__name}'


class Flight:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f'Flight: {self.__name}'


def main():
    airline = AirlineCompany('VietJet')
    print(airline)


if __name__ == '__main__':
    main()
