# Class Date

class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        self.isValid(self.__year, self.__month, self.__day)

    @staticmethod
    def isValid(year, month, day):
        if year not in range(1000, 9999 + 1):
            raise ValueError("Year is currently set as string "
                             "or exceeds the limit: [1000, 9999]")
        if month not in range(1, 12 + 1):
            raise ValueError("Month is currently set as string "
                             "or exceeds the limit: [1, 12]")
        if day not in range(1, 31 + 1):
            raise ValueError("Day is currently set as string "
                             "or exceeds the limit: [1, 31]")
        if month == 2 and day not in range(1, 28 + 1):
            raise ValueError("Month == 2 means Month is February. "
                             "This month only has 28 days")
        if month in [4, 6, 9, 11] and day not in range(1, 30 + 1):
            raise ValueError("The input month has only 30 days")

    @property
    def Date(self):
        return int(self.__year), int(self.__month), int(self.__day)

    @property
    def Year(self):  # Getter instead pf getYear()
        return self.__year

    @property
    def Month(self):  # Getter instead pf getMonth()
        return self.__month

    @property
    def Day(self):  # Getter instead pf getDay()
        return self.__day

    @Year.setter  # Setter instead pf setYear()
    def Year(self, year):
        if year not in range(1000, 9999 + 1):
            raise ValueError("Year is currently set as string "
                             "or exceeds the limit: [1000, 9999]")
        self.__year = year

    @Month.setter  # Setter instead pf setMonth()
    def Month(self, month):
        if month not in range(1, 12 + 1):
            raise ValueError("Month is currently set as string "
                             "or exceeds the limit: [1, 12]")
        if month == 2 and int(self.__day) > 28:
            raise ValueError("Month == 2 means Month is February. "
                             "This month only has 28 days")
        if month in [4, 6, 9, 11] and int(self.__day) > 30:
            raise ValueError("The input month has only 30 days")
        self.__month = month

    @Day.setter  # Setter instead pf setDay()
    def Day(self, day):
        if day not in range(1, 31 + 1):
            raise ValueError("Day is currently set as string "
                             "or exceeds the limit: [1, 31]")
        self.__day = day

    @Date.setter  # Setter instead of setDate()
    # Setter should only have (self, value)
    # So, we store the elements as tuple
    def Date(self, value):
        year, month, day = value
        self.__year = year
        self.__month = month
        self.__day = day
        self.isValid(year, month, day)

    def to_string(self):
        if int(self.__month) < 10:
            self.__month = "0" + str(self.__month)
        if int(self.__day) < 10:
            self.__day = "0" + str(self.__day)
        print(f"{str(self.__month)}/{str(self.__day)}/{str(self.__year)}")


def main():
    y, m, d = eval(input("Enter a date (y, m, d): "))
    date = Date(y, m, d)
    print(f"Year: {date.Year}, Month: {date.Month}, Day: {date.Day}")
    print("Current Date:", end=" ")
    date.to_string()
    date.Date = (2025, 10, 20)
    print("Update Date:", end=" ")
    date.to_string()
    date.Day = 30
    print("Update Day:", end=" ")
    date.to_string()
    date.Month = 4
    print("Update Month:", end=" ")
    date.Year = 1975
    print("Update Year:", end=" ")
    date.to_string()


main()
