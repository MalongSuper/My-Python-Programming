# This program displays all the leap years in the 20th century
Number_per_Line = 10
Count = 0
print("\t\t\t20th Century Leap Year")
print("-------------------------------------------------")
for Year in range(2001, 2111):
    if ((Year % 100) == 0 and (Year % 400) == 0) or ((Year % 100) != 0 and (Year % 4) == 0):
        print(format(Year, '4d'), end=" ")
        Count += 1
        if (Count % Number_per_Line) == 0:
            print()
