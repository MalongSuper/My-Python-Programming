# This program displays numbers in a pyramid pattern
print("Display numbers in a pyramid pattern")
for P in range(0, 8):  # The range should begin at zero for the top
    for S in range(7, P, -1):
        print("\t", end="")
    for S in range(0, P + 1):  # Left side pyramid
        print(format(2 ** S, '4d'), end="")
    for S in range(P - 1, -1, -1):  # Right side pyramid
        print(format(2 ** S, '4d'), end="")
    print()
