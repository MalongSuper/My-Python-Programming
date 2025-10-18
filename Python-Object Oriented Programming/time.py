# Class Time

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.validation(self.__hour, self.__minute, self.__second)

    @staticmethod
    def validation(hour, minute, second):
        if hour not in range(0, 23 + 1):
            raise ValueError("The value for hour is invalid. Limit Exceed [0, 23]")
        if minute not in range(0, 59 + 1):
            raise ValueError("The value for minute is invalid. Limit Exceed [0, 59]")
        if second not in range(0, 59 + 1):
            raise ValueError("The value for second is invalid. Limit Exceed [0, 59]")

    @property
    def Time(self):
        return int(self.__hour), int(self.__minute), int(self.__second)

    @property
    def Hour(self):
        return self.__hour

    @property
    def Minute(self):
        return self.__minute

    @property
    def Second(self):
        return self.__second

    @Time.setter  # Setter instead of setTime()
    def Time(self, time):
        hour, minute, second = time
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.validation(hour, minute, second)

    @Hour.setter  # Setter instead of setHour()
    def Hour(self, hour):
        if hour not in range(0, 23 + 1):
            raise ValueError("The value for hour is invalid. Limit Exceed [0, 23]")
        self.__hour = hour

    @Minute.setter  # Setter instead of setMinute()
    def Minute(self, minute):
        if minute not in range(0, 59 + 1):
            raise ValueError("The value for minute is invalid. Limit Exceed [0, 59]")
        self.__minute = minute

    @Second.setter  # Setter instead of setSecond()
    def Second(self, second):
        if second not in range(0, 59 + 1):
            raise ValueError("The value for second is invalid. Limit Exceed [0, 59]")
        self.__second = second

    def to_string(self):
        if int(self.__hour) < 10:
            self.__hour = "0" + str(self.__hour)
        if int(self.__minute) < 10:
            self.__minute = "0" + str(self.__minute)
        if int(self.__second) < 10:
            self.__second = "0" + str(self.__second)
        print(f"{str(self.__hour)}:{str(self.__minute)}:{str(self.__second)}")

    def nextSecond(self):
        # "23:59:59" the next is "00:00:00"
        if (self.__hour == 23 and self.__minute == 59
                and self.__second == 59):
            self.__hour = 0
            self.__minute = 0
            self.__second = 0
        # "10:59:59" the next is "11:00:00"
        elif self.__minute == 59 and self.__second == 59:
            self.__hour = int(self.__hour) + 1
            self.__minute = 0
            self.__second = 0
        # "09:45:59" the next is "09:46:00"
        elif self.__second == 59:
            self.__hour = int(self.__hour)
            self.__minute = int(self.__minute) + 1
            self.__second = 0
        else:
            self.__hour = int(self.__hour)
            self.__minute = int(self.__minute)
            self.__second = int(self.__second) + 1


def main():
    h, m, s = eval(input("Enter hour, minute, second: "))
    time = Time(h, m, s)
    print("Current Time:", end=" ")
    time.to_string()
    time.nextSecond()
    print("Next Second:", end=" ")
    time.to_string()
    time.Time = (13, 23, 23)
    print("+ Update Time:", end=" ")
    time.to_string()
    time.Hour = 15
    print("+ Update Hour:", end=" ")
    time.to_string()
    time.Minute = 45
    print("+ Update Minute:", end=" ")
    time.to_string()
    time.Second = 55
    print("+ Update Second:", end=" ")
    time.to_string()
    print("Next Second:", end=" ")
    time.nextSecond()
    time.to_string()


main()
