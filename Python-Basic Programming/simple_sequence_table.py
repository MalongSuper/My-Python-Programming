# This program displays a simple sequence table
# From 0 to n
Number_per_Line = 10
Count = 0
n = int(input("Enter n: "))
# Display the table
print("\t\t\t\tSimple Sequence Table")
print("---------------------------------------------------")
for number in range(0, n + 1):
    print(format(number, '4d'), end=" ")
    Count += 1
    if (Count % Number_per_Line) == 0:
        print()
