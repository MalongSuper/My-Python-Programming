# This program displays ten numbers that are divisible to both 5 and 6
# Assume these for lines of the table
Number_per_Line = 10
Count = 0
# Display the table
print("\tTable of Numbers divisible to both 5 and 6")
print("--------------------------------------------------")
for Number in range(100, 1001):
    if (Number % 5) == 0 and (Number % 6) == 0:
        # Display the number using format()
        print(format(Number, '4d'), end=" ")
        # Count the next number
        Count += 1
        # When the count reaches 10
        if (Count % Number_per_Line) == 0:
            # Display the next ten numbers into the next line
            print()
