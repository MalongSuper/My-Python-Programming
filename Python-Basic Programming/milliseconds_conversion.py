# This program converts milliseconds to hours:minutes:seconds
def convert_millis(millis):  # Define function
    if millis < 1000:  # 1 second = 1000 milliseconds
        seconds = millis // 1000
        print("0 : 0 :", int(seconds))
    elif 1000 <= millis < 60000:  # If it is only second, the other values are zero
        seconds = millis // 1000
        print("0 : 0 :", int(seconds))
    elif 60000 <= millis < 3600000:  # Convert to minute : second
        minute = millis // 60000
        second = (millis % 60000) / 1000
        print("0 :", int(minute), ":", int(second))
    elif millis >= 3600000:  # Convert to hour : minute : second
        hour = millis // 3600000
        minute = millis % 3600000 // 60000 % 3600000
        second = (millis % 60000) / 1000
        print(int(hour), ":", int(minute), ":", int(second))


def main():  # Define main function
    print("Milliseconds to Hour:Minute:Second")
    millis = int(input("Enter a value of milliseconds: "))
    print(millis, "milliseconds is approximately", end=" ")
    convert_millis(millis)


# Display the result
main()
