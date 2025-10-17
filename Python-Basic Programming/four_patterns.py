# This program displays four patterns using nest loops
List = {'A', 'B', 'C', 'D'}
# The program will display the pattern based on the input
print("Display four patterns")
Display = str(input("Choose the pattern you want to display: "))
if Display not in List:
    print("Pattern not found. Please try again")
else:
    # Display the pattern A
    if Display == 'A':
        print("Pattern A")
        for P in range(1, 7):
            for R in range(P):
                R += 1
                print(format(R, '2d'), end="")
            print()
    # Display the pattern B
    elif Display == 'B':
        print("Pattern B")
        for P in range(7, 1, -1):
            for R in range(P - 1):
                R += 1
                print(format(R, '2d'), end="")
            print()
    # Display the pattern C
    elif Display == 'C':
        print("Pattern C")
        for P in range(1, 7):
            for R in range(6 - P):  # This code uses to space the pattern
                print(format("  "), end="")
            for S in range(P, 0, -1):
                print(format(S, '2d'), end="")
            print()
    # Display the pattern D
    elif Display == 'D':
        print("Pattern D")
        for P in range(7, 1, -1):
            for R in range(7 - P):  # This code uses to space the pattern
                print(format("  "), end="")
            for S in range(P - 1):
                S += 1
                print(format(S, '2d'), end="")
            print()
